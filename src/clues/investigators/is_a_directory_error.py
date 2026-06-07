from clues.models import Clue, InvestigationReport, Recommendation


class IsADirectoryErrorInvestigator:
    """Investigates IsADirectoryError exceptions."""

    def can_handle(self, exc: Exception) -> bool:
        return isinstance(exc, IsADirectoryError)

    def investigate(self, exc: Exception) -> InvestigationReport:
        return InvestigationReport(
            likely_cause=(
                "Python expected a file path, but received a directory path instead."
            ),
            confidence=0.92,
            clues=[
                Clue("IsADirectoryError detected."),
                Clue(f"Original message: {exc}"),
            ],
            recommendations=[
                Recommendation("Check whether the path points to a folder instead of a file."),
                Recommendation("Provide the full file path, including the filename and extension."),
                Recommendation("If you intended to process a folder, iterate over its files first."),
                Recommendation("Use pathlib.Path(path).is_dir() to check whether a path is a directory."),
            ],
        )