from clues.models import Clue, InvestigationReport, Recommendation


class NameErrorInvestigator:
    """Investigates NameError exceptions."""

    def can_handle(self, exc: Exception) -> bool:
        return isinstance(exc, NameError)

    def investigate(self, exc: Exception) -> InvestigationReport:
        message = str(exc)

        return InvestigationReport(
            likely_cause=(
                "Python tried to use a name that has not been defined."
            ),
            confidence=0.90,
            clues=[
                Clue("NameError detected."),
                Clue(f"Original message: {message}"),
            ],
            recommendations=[
                Recommendation("Check whether the variable or function name is misspelled."),
                Recommendation("Make sure the variable is assigned before it is used."),
                Recommendation("Check whether the name exists in the current scope."),
                Recommendation("If the name comes from another module, make sure it was imported."),
            ],
        )