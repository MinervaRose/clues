from clues.models import Clue, InvestigationReport, Recommendation


class PandasKeyErrorInvestigator:
    """Investigates likely pandas DataFrame KeyError exceptions."""

    def can_handle(self, exc: Exception) -> bool:
        message = str(exc)
        return isinstance(exc, KeyError) and (
            "columns" in message.lower()
            or "not in index" in message.lower()
            or "none of" in message.lower()
        )

    def investigate(self, exc: Exception) -> InvestigationReport:
        return InvestigationReport(
            likely_cause=(
                "A pandas DataFrame operation referenced a column or index label "
                "that does not exist."
            ),
            confidence=0.88,
            clues=[
                Clue("KeyError detected with pandas-like wording."),
                Clue(f"Original message: {exc}"),
            ],
            recommendations=[
                Recommendation("Inspect available columns with df.columns."),
                Recommendation("Check for leading or trailing spaces in column names."),
                Recommendation("Verify capitalization and exact spelling."),
                Recommendation("If reading a CSV, check the separator, header row, and encoding."),
            ],
        )