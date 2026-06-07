from clues import investigate


def test_numpy_shape_error_investigation():
    exc = ValueError("operands could not be broadcast together with shapes (3,) (2,)")

    report = investigate(exc)

    assert "shape" in report.likely_cause.lower()
    assert report.confidence >= 0.8
    assert len(report.clues) >= 1
    assert len(report.recommendations) >= 1