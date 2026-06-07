"""Data models for Clues investigation reports."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Clue:
    """A piece of evidence found during an exception investigation."""

    text: str
    weight: float = 1.0


@dataclass(frozen=True)
class Recommendation:
    """A recommended debugging action."""

    text: str


@dataclass(frozen=True)
class InvestigationReport:
    """Human-readable report produced by an exception investigator."""

    likely_cause: str
    confidence: float
    clues: list[Clue] = field(default_factory=list)
    recommendations: list[Recommendation] = field(default_factory=list)

    def __str__(self) -> str:
        confidence_percent = max(0, min(100, round(self.confidence * 100)))

        lines = [
            "Investigation Report",
            "====================",
            "",
            "Likely Cause",
            "------------",
            self.likely_cause,
            "",
            "Confidence",
            "----------",
            f"{confidence_percent}%",
            "",
            "Clues",
            "-----",
        ]

        if self.clues:
            lines.extend(f"✓ {clue.text}" for clue in self.clues)
        else:
            lines.append("No specific clues were found.")

        lines.extend([
            "",
            "Recommendations",
            "---------------",
        ])

        if self.recommendations:
            lines.extend(
                f"{index}. {recommendation.text}"
                for index, recommendation in enumerate(self.recommendations, start=1)
            )
        else:
            lines.append("No specific recommendations are available yet.")

        return "\n".join(lines)
