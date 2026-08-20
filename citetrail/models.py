from dataclasses import dataclass


@dataclass(frozen=True)
class Reference:
    url: str
    title: str
    captured_at: str
    position: dict[str, int]


@dataclass(frozen=True)
class CaptureResult:
    status: str
    reference: Reference | None


@dataclass(frozen=True)
class RecallMatch:
    text: str
    reference: Reference


@dataclass(frozen=True)
class RecallResult:
    status: str
    matches: tuple[RecallMatch, ...]
