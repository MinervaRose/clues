from clues import investigate


def test_value_error_investigation():
    try:
        int("hello")
    except Exception as exc:
        report = investigate(exc)

    assert "invalid" in report.likely_cause.lower()
    assert report.confidence >= 0.8
    assert len(report.clues) >= 1
    assert len(report.recommendations) >= 1