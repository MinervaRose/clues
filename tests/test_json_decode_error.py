import json

from clues import investigate


def test_json_decode_error_investigation():
    try:
        json.loads('{"name": "Clues",}')
    except Exception as exc:
        report = investigate(exc)

    assert "json" in report.likely_cause.lower()
    assert report.confidence >= 0.8
    assert len(report.clues) >= 2
    assert len(report.recommendations) >= 1