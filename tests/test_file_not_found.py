from clues import investigate


def test_file_not_found_report_contains_filename():
    try:
        open("definitely_missing_file.csv", "r", encoding="utf-8")
    except FileNotFoundError as exc:
        report = investigate(exc)

    assert "does not exist" in report.likely_cause
    assert report.confidence >= 0.9
    assert any("definitely_missing_file.csv" in clue.text for clue in report.clues)
    assert any("working directory" in rec.text for rec in report.recommendations)
