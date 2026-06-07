from clues import investigate


def test_pandas_key_error_investigation():
    exc = KeyError("['salary'] not in index")

    report = investigate(exc)

    assert "pandas" in report.likely_cause.lower()
    assert report.confidence >= 0.8
    assert len(report.clues) >= 1
    assert len(report.recommendations) >= 1