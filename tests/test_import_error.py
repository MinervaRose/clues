from clues import investigate


def test_import_error_investigation():
    try:
        from math import pineapple
    except Exception as exc:
        report = investigate(exc)

    assert "could not import" in report.likely_cause.lower()
    assert report.confidence >= 0.8
    assert len(report.clues) >= 1
    assert len(report.recommendations) >= 1