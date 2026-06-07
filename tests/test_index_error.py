from clues import investigate


def test_index_error_investigation():
    try:
        [1, 2, 3][10]
    except Exception as exc:
        report = investigate(exc)

    assert "index" in report.likely_cause.lower()
    assert report.confidence >= 0.8
    assert len(report.clues) >= 1
    assert len(report.recommendations) >= 1