from dataclasses import dataclass

from citetrail.models import CaptureResult, Reference
from citetrail.privacy import PrivacyPolicy
from citetrail.store import Store


@dataclass(frozen=True)
class CaptureRequest:
    url: str
    title: str
    text: str
    captured_at: str


def capture(
    store: Store, request: CaptureRequest, policy: PrivacyPolicy | None = None
) -> CaptureResult:
    if not (policy or PrivacyPolicy()).allows(request.url):
        return CaptureResult(status="privacy-blocked", reference=None)
    reference = Reference(
        url=request.url,
        title=request.title,
        captured_at=request.captured_at,
        position={"start": 0, "end": len(request.text)},
    )
    store.add(request.text, reference)
    return CaptureResult(status="captured", reference=reference)
