from clues.models import Clue, InvestigationReport, Recommendation


class NumPyShapeErrorInvestigator:
    """Investigates NumPy-like shape mismatch errors."""

    def can_handle(self, exc: Exception) -> bool:
        message = str(exc).lower()
        return isinstance(exc, ValueError) and (
            "shape" in message
            or "broadcast" in message
            or "could not be broadcast" in message
            or "matmul" in message
            or "dimension mismatch" in message
        )

    def investigate(self, exc: Exception) -> InvestigationReport:
        return InvestigationReport(
            likely_cause=(
                "An array operation received inputs with incompatible shapes or dimensions."
            ),
            confidence=0.88,
            clues=[
                Clue("ValueError detected with NumPy-like shape wording."),
                Clue(f"Original message: {exc}"),
            ],
            recommendations=[
                Recommendation("Print the shapes of the arrays with array.shape."),
                Recommendation("Check whether the arrays are aligned along the expected axes."),
                Recommendation("For matrix multiplication, verify that inner dimensions match."),
                Recommendation("Use reshape, expand_dims, squeeze, or transpose only when the intended shape is clear."),
            ],
        )