from clues import investigate


def test_permission_error_investigation():
    exc = PermissionError("Permission denied: 'protected_file.txt'")

    report = investigate(exc)

    assert "permission" in report.likely_cause.lower()
    assert report.confidence >= 0.8
    assert len(report.clues) >= 1
    assert len(report.recommendations) >= 1