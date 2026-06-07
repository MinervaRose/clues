from clues import investigate


def test_type_error_investigation():
    try:
        "5" + 3
    except Exception as exc:
        report = investigate(exc)

    assert "wrong type" in report.likely_cause.lower()
    assert report.confidence >= 0.8
    assert len(report.clues) >= 1
    assert len(report.recommendations) >= 1