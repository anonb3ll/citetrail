from citetrail.models import RecallResult
from citetrail.store import Store

HONEST_STATES = frozenset({"offline", "unavailable", "privacy-blocked"})


def recall(store: Store, query: str, source_state: str = "available") -> RecallResult:
    if source_state in HONEST_STATES:
        return RecallResult(status=source_state, matches=())
    if source_state != "available":
        raise ValueError(f"unknown source state: {source_state}")
    matches = store.search(query)
    return RecallResult(status="found" if matches else "not-found", matches=matches)
