import json

from clues.models import Clue, InvestigationReport, Recommendation


class JSONDecodeErrorInvestigator:
    """Investigates JSONDecodeError exceptions."""

    def can_handle(self, exc: Exception) -> bool:
        return isinstance(exc, json.JSONDecodeError)

    def investigate(self, exc: Exception) -> InvestigationReport:
        return InvestigationReport(
            likely_cause=(
                "Python tried to parse invalid JSON."
            ),
            confidence=0.92,
            clues=[
                Clue("JSONDecodeError detected."),
                Clue(f"Original message: {exc.msg}"),
                Clue(f"Line: {exc.lineno}, column: {exc.colno}"),
            ],
            recommendations=[
                Recommendation("Check for missing commas, quotes, or closing braces."),
                Recommendation("Validate the JSON with a JSON formatter or linter."),
                Recommendation("If the JSON came from an API, inspect the raw response text."),
                Recommendation("Remember that JSON requires double quotes around strings and property names."),
            ],
        )