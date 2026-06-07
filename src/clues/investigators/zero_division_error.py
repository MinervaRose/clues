from clues.models import Clue, InvestigationReport, Recommendation


class ZeroDivisionErrorInvestigator:
    """Investigates ZeroDivisionError exceptions."""

    def can_handle(self, exc: Exception) -> bool:
        return isinstance(exc, ZeroDivisionError)

    def investigate(self, exc: Exception) -> InvestigationReport:
        message = str(exc)

        return InvestigationReport(
            likely_cause="A division operation used zero as the divisor.",
            confidence=0.95,
            clues=[
                Clue("ZeroDivisionError detected."),
                Clue(f"Original message: {message}"),
            ],
            recommendations=[
                Recommendation("Check the divisor before dividing."),
                Recommendation("Add a guard condition such as if denominator != 0."),
                Recommendation("Inspect upstream calculations that may produce zero."),
                Recommendation("Decide what should happen when division by zero occurs."),
            ],
        )