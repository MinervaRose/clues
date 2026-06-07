from clues import investigate


def test_zero_division_error_investigation():
    try:
        10 / 0
    except Exception as exc:
        report = investigate(exc)

    assert "zero" in report.likely_cause.lower()
    assert report.confidence >= 0.8
    assert len(report.clues) >= 1
    assert len(report.recommendations) >= 1