"""@file test_constants.py
@brief Tests of the Morse table and the separators (DomainConstants of DCD-001).
"""

import string

from morse_converter import MORSE_CODE_DICT
from morse_converter.domain.constants import LETTER_SEPARATOR, WORD_SEPARATOR

PUNCTUATION = ".,?'!/()&:;=+-_\"$@"


def test_table_has_every_letter_digit_and_punctuation_mark() -> None:
    expected = set(string.ascii_uppercase + string.digits + PUNCTUATION)
    assert set(MORSE_CODE_DICT) == expected


def test_table_has_54_entries() -> None:
    assert len(MORSE_CODE_DICT) == 54


def test_signal_patterns_hold_only_dots_and_dashes() -> None:
    assert all(set(code) <= {".", "-"} and code for code in MORSE_CODE_DICT.values())


def test_signal_patterns_are_unique() -> None:
    assert len(set(MORSE_CODE_DICT.values())) == len(MORSE_CODE_DICT)


def test_known_signal_patterns() -> None:
    assert MORSE_CODE_DICT["S"] == "..."
    assert MORSE_CODE_DICT["O"] == "---"
    assert MORSE_CODE_DICT["0"] == "-----"
    assert MORSE_CODE_DICT["?"] == "..--.."


def test_separators() -> None:
    assert LETTER_SEPARATOR == " "
    assert WORD_SEPARATOR == " / "
