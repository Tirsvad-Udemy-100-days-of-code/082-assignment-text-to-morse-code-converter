"""@file __main__.py
@brief Makes `python -m morse_converter` run the command line.
"""

import sys

from morse_converter.presentation.commands.convert_text_command import main

if __name__ == "__main__":
    sys.exit(main())
