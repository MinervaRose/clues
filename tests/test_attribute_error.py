from clues import investigate


def test_attribute_error_investigation():

    try:
        None.upper()
    except Exception as exc:
        report = investigate(exc)

    assert "attribute" in report.likely_cause.lower()
    assert report.confidence >= 0.8