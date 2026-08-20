from pathlib import Path

from citetrail.capture import CaptureRequest, capture
from citetrail.store import Store


def test_store_blocklist_applies_to_native_capture_policy(tmp_path: Path) -> None:
    store = Store.create(tmp_path / "store")
    store.block_host("private.example.test")

    result = capture(
        store,
        CaptureRequest(
            url="https://private.example.test/record",
            title="Synthetic private page",
            text="Never store this synthetic text.",
            captured_at="2026-08-20T22:00:00Z",
        ),
        policy=store.privacy_policy(),
    )

    assert result.status == "privacy-blocked"
    assert store.search("Never store") == ()


def test_invalid_store_policy_fails_closed(tmp_path: Path) -> None:
    store = Store.create(tmp_path / "store")
    store.policy_path.write_text("{not-json}")

    assert store.privacy_policy().rules_available is False
