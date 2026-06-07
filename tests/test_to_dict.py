from clues import investigate


def test_report_to_dict():

    try:
        {}["user_id"]
    except Exception as exc:
        report = investigate(exc)

    data = report.to_dict()

    assert isinstance(data, dict)
    assert "likely_cause" in data
    assert "confidence" in data
    assert "clues" in data
    assert "recommendations" in data

    assert data["confidence"] > 0
    assert isinstance(data["clues"], list)
    assert isinstance(
        data["recommendations"],
        list,
    )