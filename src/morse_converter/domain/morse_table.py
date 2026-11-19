"""@file morse_table.py
@brief The lookup of the signal pattern of a character (MorseTable of DCD-001).
"""

from morse_converter.domain.constants import MORSE_CODE_DICT
from morse_converter.domain.errors import UnsupportedCharacterError


def signal_pattern_for(char: str) -> str:
    """@brief Return the signal pattern of a character.

    Upper case and lower case letters have the same signal pattern.

    @param char One character of a text.
    @return The signal pattern, for example `...` for `s`.
    @throws UnsupportedCharacterError The character has no signal pattern.
    """
    try:
        return MORSE_CODE_DICT[char.upper()]
    except KeyError as err:
        raise UnsupportedCharacterError(char) from err
