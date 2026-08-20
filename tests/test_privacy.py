from pathlib import Path

from citetrail.capture import CaptureRequest, capture
from citetrail.privacy import PrivacyPolicy
from citetrail.recall import recall
from citetrail.store import Store


def test_capture_blocks_a_matching_domain_without_storing_content(tmp_path: Path) -> None:
    store = Store.create(tmp_path / "store")
    result = capture(
        store,
        CaptureRequest(
            url="https://bank.example.test/account",
            title="Account",
            text="Synthetic balance",
            captured_at="2026-08-20T12:00:00Z",
        ),
        policy=PrivacyPolicy(blocked_hosts=frozenset({"bank.example.test"})),
    )
    assert result.status == "privacy-blocked"
    assert result.reference is None
    assert recall(store, "Synthetic").status == "not-found"


def test_capture_fails_closed_when_rules_cannot_be_evaluated(tmp_path: Path) -> None:
    store = Store.create(tmp_path / "store")
    result = capture(
        store,
        CaptureRequest(
            url="https://docs.example.test/private",
            title="Synthetic page",
            text="Synthetic text",
            captured_at="2026-08-20T12:00:00Z",
        ),
        policy=PrivacyPolicy(rules_available=False),
    )
    assert result.status == "privacy-blocked"
    assert result.reference is None


def test_capture_fails_closed_for_a_malformed_url(tmp_path: Path) -> None:
    result = capture(
        Store.create(tmp_path / "store"),
        CaptureRequest(
            url="https://[malformed",
            title="Synthetic malformed page",
            text="Synthetic text",
            captured_at="2026-08-20T22:00:00Z",
        ),
    )

    assert result.status == "privacy-blocked"
    assert result.reference is None
