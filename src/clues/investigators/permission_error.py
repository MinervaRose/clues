from clues.models import Clue, InvestigationReport, Recommendation


class PermissionErrorInvestigator:
    """Investigates PermissionError exceptions."""

    def can_handle(self, exc: Exception) -> bool:
        return isinstance(exc, PermissionError)

    def investigate(self, exc: Exception) -> InvestigationReport:
        message = str(exc)

        return InvestigationReport(
            likely_cause=(
                "Python tried to access a file, folder, or resource "
                "without the required permission."
            ),
            confidence=0.90,
            clues=[
                Clue("PermissionError detected."),
                Clue(f"Original message: {message}"),
            ],
            recommendations=[
                Recommendation("Check whether the file or folder is open in another application."),
                Recommendation("Verify that your user account has read or write permissions."),
                Recommendation("Try writing to a different folder, such as the project directory."),
                Recommendation("On Windows, avoid protected folders unless running with the right permissions."),
            ],
        )