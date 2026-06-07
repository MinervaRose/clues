import csv

from clues.models import Clue, InvestigationReport, Recommendation


class CSVErrorInvestigator:
    """Investigates csv.Error exceptions."""

    def can_handle(self, exc: Exception) -> bool:
        return isinstance(exc, csv.Error)

    def investigate(self, exc: Exception) -> InvestigationReport:
        return InvestigationReport(
            likely_cause=(
                "Python encountered a problem while reading or parsing CSV data."
            ),
            confidence=0.88,
            clues=[
                Clue("csv.Error detected."),
                Clue(f"Original message: {exc}"),
            ],
            recommendations=[
                Recommendation("Check whether the file uses the expected delimiter, such as comma or semicolon."),
                Recommendation("Look for unmatched quotes or broken rows in the CSV file."),
                Recommendation("Inspect the first few lines of the file manually."),
                Recommendation("If using pandas, try specifying sep, quotechar, encoding, or engine explicitly."),
            ],
        )