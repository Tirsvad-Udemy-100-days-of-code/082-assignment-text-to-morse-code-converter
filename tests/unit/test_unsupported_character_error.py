"""@file test_unsupported_character_error.py
@brief Tests of UnsupportedCharacterError (ADR-0001).
"""

import pytest

from morse_converter.domain.errors import UnsupportedCharacterError


def test_error_holds_the_character() -> None:
    assert UnsupportedCharacterError("~").char == "~"


def test_error_message_names_the_character() -> None:
    assert "'~'" in str(UnsupportedCharacterError("~"))


def test_error_is_a_value_error() -> None:
    with pytest.raises(ValueError):
        raise UnsupportedCharacterError("~")
