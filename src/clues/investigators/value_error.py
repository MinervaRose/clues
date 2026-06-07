from clues.models import Clue, InvestigationReport, Recommendation


class ValueErrorInvestigator:
    """Investigates ValueError exceptions."""

    def can_handle(self, exc: Exception) -> bool:
        return isinstance(exc, ValueError)

    def investigate(self, exc: Exception) -> InvestigationReport:
        message = str(exc)

        return InvestigationReport(
            likely_cause=(
                "A function received a value of the right type, "
                "but the value itself was invalid."
            ),
            confidence=0.90,
            clues=[
                Clue("ValueError detected."),
                Clue(f"Original message: {message}"),
            ],
            recommendations=[
                Recommendation("Inspect the exact value being passed to the function."),
                Recommendation("Check whether the value has the expected format."),
                Recommendation("Validate or clean user input before converting it."),
                Recommendation("For conversions, test with a small known-good example first."),
            ],
        )