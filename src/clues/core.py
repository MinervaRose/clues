"""Core public investigation API."""

from __future__ import annotations

from typing import Protocol

from clues.models import Clue, InvestigationReport, Recommendation
from clues.investigators.file_not_found import FileNotFoundInvestigator
from clues.investigators.key_error import KeyErrorInvestigator
from clues.investigators.module_not_found import ModuleNotFoundInvestigator
from clues.investigators.index_error import IndexErrorInvestigator
from clues.investigators.attribute_error import (
    AttributeErrorInvestigator,
)
from clues.investigators.type_error import TypeErrorInvestigator
from clues.investigators.unicode_decode_error import UnicodeDecodeErrorInvestigator
from clues.investigators.value_error import ValueErrorInvestigator
from clues.investigators.name_error import NameErrorInvestigator
from clues.investigators.zero_division_error import ZeroDivisionErrorInvestigator
from clues.investigators.permission_error import PermissionErrorInvestigator
from clues.investigators.json_decode_error import JSONDecodeErrorInvestigator
from clues.investigators.not_implemented_error import NotImplementedErrorInvestigator
from clues.investigators.import_error import ImportErrorInvestigator
from clues.investigators.runtime_error import RuntimeErrorInvestigator
from clues.investigators.os_error import OSErrorInvestigator
from clues.investigators.is_a_directory_error import IsADirectoryErrorInvestigator
from clues.investigators.not_a_directory_error import NotADirectoryErrorInvestigator
from clues.investigators.timeout_error import TimeoutErrorInvestigator
from clues.investigators.csv_error import CSVErrorInvestigator
from clues.investigators.pandas_key_error import PandasKeyErrorInvestigator
from clues.investigators.pandas_empty_data_error import PandasEmptyDataErrorInvestigator
from clues.investigators.numpy_shape_error import NumPyShapeErrorInvestigator
from clues.investigators.cuda_out_of_memory_error import CUDAOutOfMemoryErrorInvestigator


class Investigator(Protocol):
    """Protocol implemented by all exception investigators."""

    def can_handle(self, exc: Exception) -> bool:
        """Return True when this investigator can analyze the exception."""
        ...

    def investigate(self, exc: Exception) -> InvestigationReport:
        """Return an investigation report for the exception."""
        ...


DEFAULT_INVESTIGATORS: list[Investigator] = [
    ModuleNotFoundInvestigator(),
    ImportErrorInvestigator(),
    FileNotFoundInvestigator(),
    PandasKeyErrorInvestigator(),
    KeyErrorInvestigator(),
    IndexErrorInvestigator(),
    AttributeErrorInvestigator(),
    TypeErrorInvestigator(),
    UnicodeDecodeErrorInvestigator(),
    JSONDecodeErrorInvestigator(),
    PandasEmptyDataErrorInvestigator(),
    NumPyShapeErrorInvestigator(),
    ValueErrorInvestigator(),
    NameErrorInvestigator(),
    ZeroDivisionErrorInvestigator(),
    PermissionErrorInvestigator(),
    IsADirectoryErrorInvestigator(),
    NotADirectoryErrorInvestigator(),
    TimeoutErrorInvestigator(),
    OSErrorInvestigator(),
    NotImplementedErrorInvestigator(),
    CUDAOutOfMemoryErrorInvestigator(),
    RuntimeErrorInvestigator(),
    CSVErrorInvestigator(),

]


def investigate(exc: Exception) -> InvestigationReport:
    """Investigate a Python exception and return a human-readable report.

    Parameters
    ----------
    exc:
        The exception instance to investigate.

    Returns
    -------
    InvestigationReport
        A structured report containing likely cause, confidence, clues, and
        recommended debugging actions.
    """

    for investigator in DEFAULT_INVESTIGATORS:
        if investigator.can_handle(exc):
            return investigator.investigate(exc)

    return InvestigationReport(
        likely_cause="No specific investigation is available for this exception yet.",
        confidence=0.1,
        clues=[
            Clue(f"Exception type: {type(exc).__name__}."),
            Clue(f"Exception message: {exc!s}."),
        ],
        recommendations=[
            Recommendation("Read the traceback from the bottom up."),
            Recommendation("Search for the exact exception message."),
            Recommendation("Inspect the values passed to the failing line."),
        ],
    )
