from clues.models import Clue, InvestigationReport, Recommendation


class TypeErrorInvestigator:
    """Investigates TypeError exceptions."""

    def can_handle(self, exc: Exception) -> bool:
        return isinstance(exc, TypeError)

    def investigate(self, exc: Exception) -> InvestigationReport:
        message = str(exc)

        return InvestigationReport(
            likely_cause=(
                "An operation or function was used with an object "
                "of the wrong type."
            ),
            confidence=0.90,
            clues=[
                Clue("TypeError detected."),
                Clue(f"Original message: {message}"),
            ],
            recommendations=[
                Recommendation("Check the types of the values involved."),
                Recommendation("Use type(value) to inspect unexpected objects."),
                Recommendation("Convert values explicitly when needed, for example int(x), str(x), or float(x)."),
                Recommendation("Check the function documentation for the expected argument types."),
            ],
        )