from clues import investigate


def test_unknown_exception_gets_fallback_report():
    exc = RuntimeError("Something unexpected happened")

    report = investigate(exc)

    assert "No specific investigation" in report.likely_cause
    assert report.confidence == 0.1
    assert any("RuntimeError" in clue.text for clue in report.clues)
