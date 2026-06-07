from clues.models import Clue, InvestigationReport, Recommendation


class NotADirectoryErrorInvestigator:
    """Investigates NotADirectoryError exceptions."""

    def can_handle(self, exc: Exception) -> bool:
        return isinstance(exc, NotADirectoryError)

    def investigate(self, exc: Exception) -> InvestigationReport:
        return InvestigationReport(
            likely_cause=(
                "Python expected a directory in the path, but found something else instead."
            ),
            confidence=0.92,
            clues=[
                Clue("NotADirectoryError detected."),
                Clue(f"Original message: {exc}"),
            ],
            recommendations=[
                Recommendation("Check each part of the path."),
                Recommendation("Verify that intermediate path components are folders."),
                Recommendation("Make sure you are not treating a file as if it were a directory."),
                Recommendation("Use pathlib.Path(path).is_dir() to check path components."),
            ],
        )