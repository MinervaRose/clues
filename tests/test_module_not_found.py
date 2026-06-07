from clues import investigate


def test_module_not_found_report_contains_module_name():
    exc = ModuleNotFoundError("No module named 'imaginary_package'")
    exc.name = "imaginary_package"

    report = investigate(exc)

    assert "could not find" in report.likely_cause
    assert report.confidence >= 0.8
    assert any("imaginary_package" in clue.text for clue in report.clues)
    assert any("pip install imaginary_package" in rec.text for rec in report.recommendations)
