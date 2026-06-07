from clues import investigate


def test_cuda_out_of_memory_error_investigation():
    exc = RuntimeError("CUDA out of memory. Tried to allocate 2.00 GiB.")

    report = investigate(exc)

    assert "gpu" in report.likely_cause.lower()
    assert report.confidence >= 0.8
    assert len(report.clues) >= 1
    assert len(report.recommendations) >= 1