from clues.models import Clue, InvestigationReport, Recommendation


class TimeoutErrorInvestigator:
    """Investigates TimeoutError exceptions."""

    def can_handle(self, exc: Exception) -> bool:
        return isinstance(exc, TimeoutError)

    def investigate(self, exc: Exception) -> InvestigationReport:
        return InvestigationReport(
            likely_cause=(
                "An operation took too long and exceeded its allowed time limit."
            ),
            confidence=0.90,
            clues=[
                Clue("TimeoutError detected."),
                Clue(f"Original message: {exc}"),
            ],
            recommendations=[
                Recommendation("Check whether the external service, file, network, or resource is reachable."),
                Recommendation("Increase the timeout only if the operation is expected to take longer."),
                Recommendation("Add retry logic with backoff for temporary failures."),
                Recommendation("Log timing information to identify where the delay occurs."),
            ],
        )