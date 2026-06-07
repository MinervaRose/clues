from clues import investigate


def test_unicode_decode_error_investigation():
    try:
        b"\xff".decode("utf-8")
    except Exception as exc:
        report = investigate(exc)

    assert "encoding" in report.likely_cause.lower()
    assert report.confidence >= 0.8
    assert len(report.clues) >= 2
    assert len(report.recommendations) >= 1