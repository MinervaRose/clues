from clues.models import Clue, InvestigationReport, Recommendation


class RuntimeErrorInvestigator:
    """Investigates RuntimeError exceptions."""

    def can_handle(self, exc: Exception) -> bool:
        return (
            isinstance(exc, RuntimeError)
            and not isinstance(exc, NotImplementedError)
        )

    def investigate(self, exc: Exception) -> InvestigationReport:
        return InvestigationReport(
            likely_cause=(
                "The program encountered a runtime condition "
                "that prevented it from continuing."
            ),
            confidence=0.75,
            clues=[
                Clue("RuntimeError detected."),
                Clue(f"Original message: {exc}"),
            ],
            recommendations=[
                Recommendation(
                    "Inspect the full traceback."
                ),
                Recommendation(
                    "Look for the operation immediately before the error."
                ),
                Recommendation(
                    "Check whether the program state is valid."
                ),
                Recommendation(
                    "Search for framework-specific guidance if applicable."
                ),
            ],
        )