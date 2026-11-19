"""@file constants.py
@brief The texts and exit codes of the command line (PresentationConstants of DCD-001).
"""

## @brief The prompt shown when no text is given as an argument.
PROMPT_TEXT: str = "Text to convert: "

## @brief The start of the message for an unsupported character; the character follows.
ERROR_MESSAGE: str = "Unsupported character:"

## @brief The exit code of a successful run.
EXIT_OK: int = 0

## @brief The exit code of a run that ended with an error.
EXIT_ERROR: int = 1
