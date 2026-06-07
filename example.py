from clues import investigate

try:
    user = {"name": "Ada"}
    print(user["email"])
except Exception as exc:
    report = investigate(exc)
    print(report)
