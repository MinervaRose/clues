import csv

from clues import investigate


def test_csv_error_investigation():
    exc = csv.Error("newline inside string")

    report = investigate(exc)

    assert "csv" in report.likely_cause.lower()
    assert report.confidence >= 0.8
    assert len(report.clues) >= 1
    assert len(report.recommendations) >= 1