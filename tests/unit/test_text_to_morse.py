"""@file test_text_to_morse.py
@brief Tests of the use case text_to_morse against the postconditions of OC-001.
"""

import pytest

from morse_converter import text_to_morse
from morse_converter.domain.errors import UnsupportedCharacterError


def test_one_word() -> None:
    assert text_to_morse("SOS") == "... --- ..."


def test_two_words_are_separated_by_a_slash() -> None:
    assert text_to_morse("Hello World") == (
        ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
    )


def test_lower_case_gives_the_same_morse_code() -> None:
    assert text_to_morse("sos") == text_to_morse("SOS")


def test_digits_and_punctuation() -> None:
    assert text_to_morse("Call 112!") == "-.-. .- .-.. .-.. / .---- .---- ..--- -.-.--"


def test_empty_text_gives_empty_morse_code() -> None:
    assert text_to_morse("") == ""


def test_blank_text_gives_empty_morse_code() -> None:
    assert text_to_morse("  \t\n ") == ""


def test_runs_of_white_space_count_as_one_word_separator() -> None:
    assert text_to_morse("a   b\t\nc") == ".- / -... / -.-."


def test_no_leading_or_trailing_space() -> None:
    assert text_to_morse("  e  ") == "."


def test_unsupported_character_rejects_the_whole_text() -> None:
    with pytest.raises(UnsupportedCharacterError) as raised:
        text_to_morse("ok ~ fine")
    assert raised.value.char == "~"


def test_package_exports_the_names_of_the_assignment() -> None:
    import morse_converter

    assert morse_converter.__all__ == ["MORSE_CODE_DICT", "text_to_morse"]
