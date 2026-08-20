from pathlib import Path

from citetrail.capture import CaptureRequest, capture
from citetrail.recall import recall
from citetrail.store import Store


def test_recall_returns_matching_text_only_with_its_reference(tmp_path: Path) -> None:
    store = Store.create(tmp_path / "store")
    capture(
        store,
        CaptureRequest(
            url="https://docs.example.test/retry",
            title="Retry guide",
            text="Use exponential retry backoff for transient failures.",
            captured_at="2026-08-20T12:00:00Z",
        ),
    )

    result = recall(store, "backoff")

    assert result.status == "found"
    assert len(result.matches) == 1
    assert result.matches[0].text == "Use exponential retry backoff for transient failures."
    assert result.matches[0].reference.url == "https://docs.example.test/retry"
    assert result.matches[0].reference.position == {"start": 0, "end": 53}
