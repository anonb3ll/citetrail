import json
import sqlite3
from dataclasses import dataclass
from pathlib import Path

from citetrail.models import RecallMatch, Reference
from citetrail.privacy import PrivacyPolicy


@dataclass(frozen=True)
class Store:
    path: Path

    @classmethod
    def create(cls, directory: Path) -> "Store":
        directory.mkdir(parents=True, exist_ok=True)
        store = cls(directory / "citetrail.sqlite3")
        with store.connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS captures (
                    id INTEGER PRIMARY KEY,
                    url TEXT NOT NULL,
                    title TEXT NOT NULL,
                    captured_at TEXT NOT NULL,
                    text TEXT NOT NULL,
                    position_start INTEGER NOT NULL,
                    position_end INTEGER NOT NULL
                )
                """
            )
        return store

    def connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.path)

    @property
    def policy_path(self) -> Path:
        return self.path.parent / "policy.json"

    def privacy_policy(self) -> PrivacyPolicy:
        if not self.policy_path.exists():
            return PrivacyPolicy()
        try:
            values = json.loads(self.policy_path.read_text())
        except (OSError, json.JSONDecodeError):
            return PrivacyPolicy(rules_available=False)
        if not isinstance(values, dict):
            return PrivacyPolicy(rules_available=False)
        return PrivacyPolicy.from_mapping(values)

    def block_host(self, host: str) -> None:
        policy = self.privacy_policy()
        if not policy.rules_available:
            raise ValueError("cannot update an invalid policy file")
        blocked_hosts = sorted(policy.blocked_hosts | {host.lower()})
        self.policy_path.write_text(json.dumps({"blocked_hosts": blocked_hosts}, indent=2) + "\n")

    def add(self, text: str, reference: Reference) -> None:
        with self.connect() as connection:
            connection.execute(
                """
                INSERT INTO captures (
                    url, title, captured_at, text, position_start, position_end
                ) VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    reference.url,
                    reference.title,
                    reference.captured_at,
                    text,
                    reference.position["start"],
                    reference.position["end"],
                ),
            )

    def search(self, query: str) -> tuple[RecallMatch, ...]:
        with self.connect() as connection:
            rows = connection.execute(
                """
                SELECT text, url, title, captured_at, position_start, position_end
                FROM captures
                WHERE text LIKE ? OR title LIKE ?
                ORDER BY id DESC
                """,
                (f"%{query}%", f"%{query}%"),
            ).fetchall()
        return tuple(
            RecallMatch(
                text=row[0],
                reference=Reference(
                    url=row[1],
                    title=row[2],
                    captured_at=row[3],
                    position={"start": row[4], "end": row[5]},
                ),
            )
            for row in rows
        )
