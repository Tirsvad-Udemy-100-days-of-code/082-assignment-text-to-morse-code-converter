**English** · [Dansk](Summary-da) · [Bahasa Malaysia](Summary-ms)

# What the steps taught

- Start a project with a use case and a design, then code from the design.
- A `.venv`, `python -m pip install --upgrade pip` and an editable install give a repeatable set-up.
- A dictionary maps characters to Morse code; `str.upper()`, `str.split()` and `str.join()` do the conversion.
- A specific exception (`UnsupportedCharacterError`) tells the caller what is wrong, and `raise ... from` keeps the cause.
- `python -m morse_converter` takes arguments or a prompt, and returns exit code 0 or 1.
- pytest tests the units and runs the program as a subprocess; a notebook runs the same steps.

Examples: `SOS` is `... --- ...`; `Hello World` is `.... . .-.. .-.. --- / .-- --- .-. .-.. -..`; `~` is not supported and gives exit code 1.
