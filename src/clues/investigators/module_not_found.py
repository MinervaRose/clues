"""Investigator for ModuleNotFoundError exceptions."""

from __future__ import annotations

from clues.models import Clue, InvestigationReport, Recommendation


class ModuleNotFoundInvestigator:
    """Investigate missing import/module errors."""

    def can_handle(self, exc: Exception) -> bool:
        return isinstance(exc, ModuleNotFoundError)

    def investigate(self, exc: Exception) -> InvestigationReport:
        module_name = getattr(exc, "name", None)
        clues = [Clue("ModuleNotFoundError detected.")]

        if module_name:
            clues.append(Clue(f"Missing module: {module_name}."))
        else:
            clues.append(Clue(f"Exception message: {exc!s}."))

        recommendations = [
            Recommendation("Check whether the module name is spelled correctly."),
            Recommendation("Verify that your virtual environment is activated."),
            Recommendation("Install the missing package if it is an external dependency."),
            Recommendation("If it is a local module, check your project structure and current working directory."),
        ]

        if module_name:
            recommendations.insert(
                2,
                Recommendation(f"Try installing it with: python -m pip install {module_name}"),
            )

        return InvestigationReport(
            likely_cause="Python could not find the module you tried to import.",
            confidence=0.9,
            clues=clues,
            recommendations=recommendations,
        )
