from clues.models import Clue, InvestigationReport, Recommendation


class OSErrorInvestigator:
    """Investigates generic OSError exceptions."""

    def can_handle(self, exc: Exception) -> bool:
        return isinstance(exc, OSError)

    def investigate(self, exc: Exception) -> InvestigationReport:
        return InvestigationReport(
            likely_cause=(
                "Python encountered an operating system related error, "
                "often involving files, paths, permissions, or resources."
            ),
            confidence=0.75,
            clues=[
                Clue("OSError detected."),
                Clue(f"Original message: {exc}"),
            ],
            recommendations=[
                Recommendation("Check whether the file path or resource exists."),
                Recommendation("Verify permissions for the file, folder, or resource."),
                Recommendation("Inspect the full error message for an errno or system-specific hint."),
                Recommendation("Check whether the resource is locked, unavailable, or already in use."),
            ],
        )