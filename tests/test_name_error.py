from clues import investigate


def test_name_error_investigation():
    try:
        unknown_variable
    except Exception as exc:
        report = investigate(exc)

    assert "not been defined" in report.likely_cause.lower()
    assert report.confidence >= 0.8
    assert len(report.clues) >= 1
    assert len(report.recommendations) >= 1