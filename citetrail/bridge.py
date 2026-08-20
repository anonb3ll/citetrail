from dataclasses import dataclass

from citetrail.capture import CaptureRequest, capture
from citetrail.models import CaptureResult
from citetrail.privacy import PrivacyPolicy
from citetrail.store import Store

DOCUMENTED_MAX_CAPTURE_CHARS = 50_000


@dataclass(frozen=True)
class BridgeResult:
    status: str
    capture: CaptureResult | None
    truncated: bool
    gap: bool


class NativeBridge:
    def __init__(
        self, service_available: bool = True, max_capture_chars: int = DOCUMENTED_MAX_CAPTURE_CHARS
    ) -> None:
        self.service_available = service_available
        self.max_capture_chars = max_capture_chars
        self.terminated = False

    def terminate(self) -> None:
        self.terminated = True

    def capture(
        self, store: Store, request: CaptureRequest, policy: PrivacyPolicy | None = None
    ) -> BridgeResult:
        if not self.service_available or self.terminated:
            return BridgeResult(
                status="unavailable", capture=None, truncated=False, gap=self.terminated
            )
        truncated = len(request.text) > self.max_capture_chars
        bounded_request = CaptureRequest(
            url=request.url,
            title=request.title,
            text=request.text[: self.max_capture_chars],
            captured_at=request.captured_at,
        )
        capture_result = capture(store, bounded_request, policy=policy)
        return BridgeResult(
            status=capture_result.status,
            capture=capture_result,
            truncated=truncated,
            gap=False,
        )
