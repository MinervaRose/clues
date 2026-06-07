from clues.models import Clue, InvestigationReport, Recommendation


class UnicodeDecodeErrorInvestigator:
    """Investigates UnicodeDecodeError exceptions."""

    def can_handle(self, exc: Exception) -> bool:
        return isinstance(exc, UnicodeDecodeError)

    def investigate(self, exc: Exception) -> InvestigationReport:
        return InvestigationReport(
            likely_cause=(
                "Python tried to read text using the wrong character encoding."
            ),
            confidence=0.92,
            clues=[
                Clue("UnicodeDecodeError detected."),
                Clue(f"Encoding used: {exc.encoding}"),
                Clue(f"Problem near byte position: {exc.start}"),
                Clue(f"Original message: {exc}"),
            ],
            recommendations=[
                Recommendation("Try opening the file with encoding='utf-8'."),
                Recommendation("If that fails, try encoding='latin-1' or encoding='cp1252'."),
                Recommendation("For CSV files, pass the encoding explicitly when reading the file."),
                Recommendation("Check the file source to identify the correct encoding."),
            ],
        )