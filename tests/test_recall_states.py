from pathlib import Path

import pytest

from citetrail.recall import recall
from citetrail.store import Store


@pytest.mark.parametrize("source_state", ["offline", "unavailable", "privacy-blocked"])
def test_recall_preserves_non_found_states(tmp_path: Path, source_state: str) -> None:
    result = recall(Store.create(tmp_path / "store"), "anything", source_state=source_state)

    assert result.status == source_state
    assert result.matches == ()


def test_recall_reports_not_found_when_the_store_has_no_match(tmp_path: Path) -> None:
    result = recall(Store.create(tmp_path / "store"), "anything")

    assert result.status == "not-found"
