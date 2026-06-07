from clues import investigate


def test_timeout_error_investigation():
    exc = TimeoutError("The operation timed out.")

    report = investigate(exc)

    assert "too long" in report.likely_cause.lower()
    assert report.confidence >= 0.8
    assert len(report.clues) >= 1
    assert len(report.recommendations) >= 1