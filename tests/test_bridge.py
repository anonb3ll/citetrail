from pathlib import Path

from citetrail.bridge import NativeBridge
from citetrail.capture import CaptureRequest
from citetrail.privacy import PrivacyPolicy
from citetrail.store import Store


def request(text: str = "Synthetic browser text") -> CaptureRequest:
    return CaptureRequest(
        url="https://docs.example.test/page",
        title="Synthetic page",
        text=text,
        captured_at="2026-08-20T12:00:00Z",
    )


def test_bridge_reports_unavailable_when_the_local_service_is_down(tmp_path: Path) -> None:
    result = NativeBridge(service_available=False).capture(
        Store.create(tmp_path / "store"), request()
    )

    assert result.status == "unavailable"
    assert result.capture is None
    assert result.gap is False


def test_bridge_truncates_oversize_pages_at_its_documented_boundary(tmp_path: Path) -> None:
    result = NativeBridge(max_capture_chars=12).capture(
        Store.create(tmp_path / "store"),
        request("Synthetic page content is longer than twelve characters."),
    )

    assert result.status == "captured"
    assert result.truncated is True
    assert result.capture is not None
    assert result.capture.reference is not None
    assert result.capture.reference.position == {"start": 0, "end": 12}


def test_bridge_termination_leaves_a_visible_gap(tmp_path: Path) -> None:
    bridge = NativeBridge()
    bridge.terminate()

    result = bridge.capture(Store.create(tmp_path / "store"), request())

    assert result.status == "unavailable"
    assert result.gap is True


def test_bridge_reports_privacy_blocked_without_storing_content(tmp_path: Path) -> None:
    store = Store.create(tmp_path / "store")
    result = NativeBridge().capture(
        store,
        request(),
        policy=PrivacyPolicy(blocked_hosts=frozenset({"docs.example.test"})),
    )

    assert result.status == "privacy-blocked"
    assert result.capture is not None
    assert result.capture.status == "privacy-blocked"
    assert store.search("Synthetic browser text") == ()
