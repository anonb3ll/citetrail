from pathlib import Path

from citetrail.capture import CaptureRequest, capture
from citetrail.mcp import search_tool
from citetrail.store import Store


def test_mcp_search_returns_fragments_with_required_provenance(tmp_path: Path) -> None:
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

    payload = search_tool(store, "backoff")

    assert payload["status"] == "found"
    assert payload["matches"] == [
        {
            "text": "Use exponential retry backoff for transient failures.",
            "reference": {
                "url": "https://docs.example.test/retry",
                "title": "Retry guide",
                "captured_at": "2026-08-20T12:00:00Z",
                "position": {"start": 0, "end": 53},
            },
        }
    ]
