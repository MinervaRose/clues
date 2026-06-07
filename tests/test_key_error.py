from clues import investigate


def test_key_error_report_contains_missing_key():
    exc = KeyError("email")

    report = investigate(exc)

    assert "email" in report.likely_cause
    assert report.confidence >= 0.9
    assert any("KeyError" in clue.text for clue in report.clues)
    assert any("data.keys()" in rec.text for rec in report.recommendations)
