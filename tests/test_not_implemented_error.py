from clues import investigate


def test_not_implemented_error_investigation():
    try:
        raise NotImplementedError("TODO: add model training logic")
    except Exception as exc:
        report = investigate(exc)

    assert "not been implemented" in report.likely_cause.lower()
    assert report.confidence >= 0.8
    assert len(report.clues) >= 1
    assert len(report.recommendations) >= 1