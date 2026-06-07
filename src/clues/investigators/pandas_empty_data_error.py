from clues.models import Clue, InvestigationReport, Recommendation


class PandasEmptyDataErrorInvestigator:
    """Investigates pandas EmptyDataError-like exceptions."""

    def can_handle(self, exc: Exception) -> bool:
        return (
            type(exc).__name__ == "EmptyDataError"
            or "no columns to parse from file" in str(exc).lower()
        )

    def investigate(self, exc: Exception) -> InvestigationReport:
        return InvestigationReport(
            likely_cause=(
                "Pandas tried to read a file, but found no columns or usable data."
            ),
            confidence=0.88,
            clues=[
                Clue("Pandas EmptyDataError-like exception detected."),
                Clue(f"Original message: {exc}"),
            ],
            recommendations=[
                Recommendation("Check whether the file is empty."),
                Recommendation("Verify that the file path points to the expected file."),
                Recommendation("Open the file manually and inspect the first few lines."),
                Recommendation("Check whether the delimiter, header row, or encoding is correct."),
            ],
        )