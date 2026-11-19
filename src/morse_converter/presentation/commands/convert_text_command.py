"""@file convert_text_command.py
@brief The command line of the use case (ConvertTextCommand of DCD-001).
"""

import sys
from collections.abc import Sequence

from morse_converter.application.use_cases.text_to_morse import text_to_morse
from morse_converter.domain.errors import UnsupportedCharacterError
from morse_converter.presentation.constants import (
    ERROR_MESSAGE,
    EXIT_ERROR,
    EXIT_OK,
    PROMPT_TEXT,
)


def read_text(arguments: Sequence[str]) -> str:
    """@brief Get the text from the arguments or from a prompt.

    @param arguments The program arguments, without the program name.
    @return The arguments joined by one space, or the line typed at the prompt when
            there are no arguments.
    """
    if arguments:
        return " ".join(arguments)
    return input(PROMPT_TEXT)


def run(arguments: Sequence[str]) -> int:
    """@brief Convert the text and show the morse code or the error.

    @param arguments The program arguments, without the program name.
    @return `EXIT_OK` when the morse code was printed, `EXIT_ERROR` when a character
            is not supported (the message names it and goes to the error stream).
    """
    text = read_text(arguments)
    try:
        morse = text_to_morse(text)
    except UnsupportedCharacterError as err:
        print(f"{ERROR_MESSAGE} {err.char!r}", file=sys.stderr)
        return EXIT_ERROR
    print(morse)
    return EXIT_OK


def main() -> int:
    """@brief Entry point: run the command with the program arguments.

    @return The exit code of `run`.
    """
    return run(sys.argv[1:])
