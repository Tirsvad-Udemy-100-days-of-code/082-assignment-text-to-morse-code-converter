"""@file __init__.py
@brief The package `morse_converter`: convert a text to Morse code.

Exports the names of the assignment, `text_to_morse` and `MORSE_CODE_DICT`.
"""

from morse_converter.application.use_cases.text_to_morse import text_to_morse
from morse_converter.domain.constants import MORSE_CODE_DICT

__all__ = ["MORSE_CODE_DICT", "text_to_morse"]
