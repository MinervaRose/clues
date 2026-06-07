"""Investigator for FileNotFoundError exceptions."""

from __future__ import annotations

from clues.models import Clue, InvestigationReport, Recommendation


class FileNotFoundInvestigator:
    """Investigate missing file or directory errors."""

    def can_handle(self, exc: Exception) -> bool:
        return isinstance(exc, FileNotFoundError)

    def investigate(self, exc: Exception) -> InvestigationReport:
        filename = getattr(exc, "filename", None)
        clues = [Clue("FileNotFoundError detected.")]

        if filename:
            clues.append(Clue(f"Missing path: {filename}."))
        else:
            clues.append(Clue(f"Exception message: {exc!s}."))

        return InvestigationReport(
            likely_cause="The requested file or directory does not exist at the path Python tried to open.",
            confidence=0.95,
            clues=clues,
            recommendations=[
                Recommendation("Check that the file path is spelled correctly."),
                Recommendation("Verify your current working directory."),
                Recommendation("Use an absolute path temporarily while debugging."),
                Recommendation("Confirm that the file has been created or downloaded before this line runs."),
            ],
        )
