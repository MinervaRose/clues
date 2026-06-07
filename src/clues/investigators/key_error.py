"""Investigator for KeyError exceptions."""

from __future__ import annotations

from clues.models import Clue, InvestigationReport, Recommendation


class KeyErrorInvestigator:
    """Investigate missing dictionary key errors."""

    def can_handle(self, exc: Exception) -> bool:
        return isinstance(exc, KeyError)

    def investigate(self, exc: Exception) -> InvestigationReport:
        missing_key = exc.args[0] if exc.args else "<unknown>"

        return InvestigationReport(
            likely_cause=f"A dictionary-like object does not contain the key {missing_key!r}.",
            confidence=0.95,
            clues=[
                Clue("KeyError detected."),
                Clue(f"Missing key: {missing_key!r}."),
            ],
            recommendations=[
                Recommendation("Print or inspect the available keys with data.keys()."),
                Recommendation("Check whether the key name is misspelled."),
                Recommendation("Use data.get(key) when the key is optional."),
                Recommendation("Verify that upstream data contains the expected field."),
            ],
        )
