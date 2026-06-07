from clues import investigate


def test_runtime_error_investigation():

    try:
        raise RuntimeError("Something went wrong.")
    except Exception as exc:
        report = investigate(exc)

    assert "runtime" in report.likely_cause.lower()
    assert report.confidence >= 0.7