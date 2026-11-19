"""@file text_to_morse.py
@brief The use case that converts a text to morse code (TextToMorseUseCase of DCD-001).
"""

from morse_converter.domain.constants import LETTER_SEPARATOR, WORD_SEPARATOR
from morse_converter.domain.morse_table import signal_pattern_for


def text_to_morse(text: str) -> str:
    """@brief Convert a text to morse code.

    The signal patterns of the characters of a word are separated by one space and
    the words by ` / `. Any run of white space between words counts as one word
    separator and white space at the start or the end is ignored, so a blank text
    gives an empty morse code.

    @param text The text to convert.
    @return The morse code of the text, for example `... --- ...` for `SOS`.
    @throws UnsupportedCharacterError A character of the text has no signal pattern.
    """
    words = text.split()
    return WORD_SEPARATOR.join(
        LETTER_SEPARATOR.join(signal_pattern_for(char) for char in word)
        for word in words
    )
