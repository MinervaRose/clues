from clues.models import (
    Clue,
    InvestigationReport,
    Recommendation,
)


class AttributeErrorInvestigator:
    """Investigates AttributeError exceptions."""

    def can_handle(self, exc: Exception) -> bool:
        return isinstance(exc, AttributeError)

    def investigate(self, exc: Exception) -> InvestigationReport:

        message = str(exc)

        return InvestigationReport(
            likely_cause=(
                "An object does not have the requested "
                "attribute or method."
            ),
            confidence=0.90,
            clues=[
                Clue("AttributeError detected."),
                Clue(f"Original message: {message}"),
            ],
            recommendations=[
                Recommendation(
                    "Check that the object is the expected type."
                ),
                Recommendation(
                    "Verify the spelling of the attribute or method."
                ),
                Recommendation(
                    "Use print(type(object)) to inspect the object."
                ),
                Recommendation(
                    "Check whether the object is None."
                ),
            ],
        )