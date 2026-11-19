"""@file test_morse_table.py
@brief Tests of MorseTable.signal_pattern_for.
"""

import pytest

from morse_converter.domain.errors import UnsupportedCharacterError
from morse_converter.domain.morse_table import signal_pattern_for


def test_signal_pattern_of_a_letter() -> None:
    assert signal_pattern_for("A") == ".-"


def test_upper_and_lower_case_have_the_same_signal_pattern() -> None:
    assert signal_pattern_for("a") == signal_pattern_for("A")


def test_signal_pattern_of_a_digit() -> None:
    assert signal_pattern_for("7") == "--..."


def test_signal_pattern_of_a_punctuation_mark() -> None:
    assert signal_pattern_for("@") == ".--.-."


@pytest.mark.parametrize("char", ["~", "é", "#", "\t", " ", "\n"])
def test_unsupported_character_is_rejected(char: str) -> None:
    with pytest.raises(UnsupportedCharacterError) as raised:
        signal_pattern_for(char)
    assert raised.value.char == char
