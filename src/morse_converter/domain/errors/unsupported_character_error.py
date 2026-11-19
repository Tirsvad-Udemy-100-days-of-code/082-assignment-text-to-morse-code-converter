"""@file unsupported_character_error.py
@brief The error for a character without a signal pattern (DCD-001).
"""


class UnsupportedCharacterError(ValueError):
    """@brief A character of the text has no signal pattern (ADR-0001)."""

    def __init__(self, char: str) -> None:
        """@brief Create the error and name the character.

        @param char The character that has no signal pattern.
        """
        super().__init__(f"No signal pattern for the character {char!r}")
        ## @brief The character that is not supported.
        self.char = char
