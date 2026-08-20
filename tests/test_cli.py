from pathlib import Path

from citetrail.capture import CaptureRequest, capture
from citetrail.cli import main
from citetrail.store import Store


def test_init_creates_a_local_store(tmp_path: Path) -> None:
    exit_code = main(["init", "--store", str(tmp_path / "store")])

    assert exit_code == 0
    assert (tmp_path / "store" / "citetrail.sqlite3").is_file()


def test_search_prints_matching_text_with_its_provenance(tmp_path: Path, capsys: object) -> None:
    store_path = tmp_path / "store"
    store = Store.create(store_path)
    capture(
        store,
        CaptureRequest(
            url="https://docs.example.test/retry",
            title="Retry guide",
            text="Use exponential retry backoff for transient failures.",
            captured_at="2026-08-20T12:00:00Z",
        ),
    )

    exit_code = main(["search", "backoff", "--store", str(store_path)])

    assert exit_code == 0
    assert "https://docs.example.test/retry" in capsys.readouterr().out


def test_block_adds_a_host_to_the_local_privacy_policy(tmp_path: Path) -> None:
    store_path = tmp_path / "store"

    exit_code = main(["block", "private.example.test", "--store", str(store_path)])

    assert exit_code == 0
    assert "private.example.test" in Store.create(store_path).privacy_policy().blocked_hosts
