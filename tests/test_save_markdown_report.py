from clues import investigate


def test_report_save_markdown(tmp_path):
    try:
        {}["user_id"]
    except Exception as exc:
        report = investigate(exc)

    output_path = tmp_path / "report.md"

    report.save_markdown(str(output_path))

    content = output_path.read_text(encoding="utf-8")

    assert output_path.exists()
    assert "# Investigation Report" in content
    assert "user_id" in content