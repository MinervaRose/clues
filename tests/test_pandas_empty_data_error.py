from clues import investigate


class EmptyDataError(Exception):
    pass


def test_pandas_empty_data_error_investigation():
    exc = EmptyDataError("No columns to parse from file")

    report = investigate(exc)

    assert "pandas" in report.likely_cause.lower()
    assert report.confidence >= 0.8
    assert len(report.clues) >= 1
    assert len(report.recommendations) >= 1