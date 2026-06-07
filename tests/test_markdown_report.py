from clues import investigate


def test_report_to_markdown():
    try:
        {}["user_id"]
    except Exception as exc:
        report = investigate(exc)

    markdown = report.to_markdown()

    assert "# Investigation Report" in markdown
    assert "## Likely Cause" in markdown
    assert "## Clues" in markdown
    assert "## Recommendations" in markdown
    assert "user_id" in markdown