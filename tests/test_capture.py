from pathlib import Path

from citetrail.capture import CaptureRequest, capture
from citetrail.store import Store


def test_capture_stores_fragment_with_its_bounded_reference(tmp_path: Path) -> None:
    store = Store.create(tmp_path / "store")

    result = capture(
        store,
        CaptureRequest(
            url="https://docs.example.test/retry",
            title="Retry guide",
            text="Use exponential retry backoff for transient failures.",
            captured_at="2026-08-20T12:00:00Z",
        ),
    )

    assert result.status == "captured"
    assert result.reference.url == "https://docs.example.test/retry"
    assert result.reference.title == "Retry guide"
    assert result.reference.captured_at == "2026-08-20T12:00:00Z"
    assert result.reference.position == {"start": 0, "end": 53}
