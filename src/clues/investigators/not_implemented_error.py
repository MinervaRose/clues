from clues.models import Clue, InvestigationReport, Recommendation


class NotImplementedErrorInvestigator:
    """Investigates NotImplementedError exceptions."""

    def can_handle(self, exc: Exception) -> bool:
        return isinstance(exc, NotImplementedError)

    def investigate(self, exc: Exception) -> InvestigationReport:
        message = str(exc)

        return InvestigationReport(
            likely_cause=(
                "The code reached a function, method, or feature "
                "that has not been implemented yet."
            ),
            confidence=0.92,
            clues=[
                Clue("NotImplementedError detected."),
                Clue(f"Original message: {message}" if message else "No custom message provided."),
            ],
            recommendations=[
                Recommendation("Look for placeholder code containing 'raise NotImplementedError'."),
                Recommendation("Implement the missing function or method."),
                Recommendation("Check whether a subclass is expected to override this method."),
                Recommendation("If using a template project, verify which sections are intentionally incomplete."),
            ],
        )