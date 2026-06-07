from clues.models import Clue, InvestigationReport, Recommendation


class ImportErrorInvestigator:
    """Investigates ImportError exceptions."""

    def can_handle(self, exc: Exception) -> bool:
        return isinstance(exc, ImportError) and not isinstance(exc, ModuleNotFoundError)

    def investigate(self, exc: Exception) -> InvestigationReport:
        message = str(exc)

        return InvestigationReport(
            likely_cause=(
                "Python found the module, but could not import the requested "
                "name, object, or component."
            ),
            confidence=0.90,
            clues=[
                Clue("ImportError detected."),
                Clue(f"Original message: {message}"),
            ],
            recommendations=[
                Recommendation("Check whether the imported name exists in that module."),
                Recommendation("Verify the spelling and capitalization of the imported name."),
                Recommendation("Check for circular imports between files."),
                Recommendation("Make sure you are importing from the expected package or local file."),
            ],
        )