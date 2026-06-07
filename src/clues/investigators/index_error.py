from clues.models import Clue, InvestigationReport, Recommendation


class IndexErrorInvestigator:
    """Investigates IndexError exceptions."""

    def can_handle(self, exc: Exception) -> bool:
        return isinstance(exc, IndexError)

    def investigate(self, exc: Exception) -> InvestigationReport:
        return InvestigationReport(
            likely_cause="A sequence was accessed with an index that does not exist.",
            confidence=0.9,
            clues=[
                Clue("IndexError detected."),
                Clue(f"Original message: {exc}"),
            ],
            recommendations=[
                Recommendation("Check the length of the list, tuple, or sequence before indexing."),
                Recommendation("Remember that Python indices start at 0."),
                Recommendation("Use a loop or conditional check to avoid accessing missing positions."),
                Recommendation("If you need the last item, use sequence[-1] only when the sequence is not empty."),
            ],
        )