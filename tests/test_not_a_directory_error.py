from clues import investigate


def test_not_a_directory_error_investigation():
    exc = NotADirectoryError("Not a directory: 'data.csv/file.txt'")

    report = investigate(exc)

    assert "directory" in report.likely_cause.lower()
    assert report.confidence >= 0.8
    assert len(report.clues) >= 1
    assert len(report.recommendations) >= 1