from clues import investigate


def test_os_error_investigation():
    exc = OSError("Generic OS-level error")

    report = investigate(exc)

    assert "operating system" in report.likely_cause.lower()
    assert report.confidence >= 0.7
    assert len(report.clues) >= 1
    assert len(report.recommendations) >= 1