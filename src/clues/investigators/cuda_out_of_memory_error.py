from clues.models import Clue, InvestigationReport, Recommendation


class CUDAOutOfMemoryErrorInvestigator:
    """Investigates CUDA out-of-memory errors."""

    def can_handle(self, exc: Exception) -> bool:
        message = str(exc).lower()
        return isinstance(exc, RuntimeError) and (
            "cuda out of memory" in message
            or "cuda error: out of memory" in message
            or "outofmemoryerror" in message
        )

    def investigate(self, exc: Exception) -> InvestigationReport:
        return InvestigationReport(
            likely_cause="The GPU does not have enough available memory for the operation.",
            confidence=0.90,
            clues=[
                Clue("RuntimeError detected with CUDA out-of-memory wording."),
                Clue(f"Original message: {exc}"),
            ],
            recommendations=[
                Recommendation("Reduce the batch size."),
                Recommendation("Restart the runtime or process to clear GPU memory."),
                Recommendation("Use mixed precision if appropriate."),
                Recommendation("Delete unused tensors and call torch.cuda.empty_cache() when using PyTorch."),
                Recommendation("Use a smaller model or enable gradient checkpointing for training."),
            ],
        )