**English** · [Dansk](Step-2-Morse-Table-da) · [Bahasa Malaysia](Step-2-Morse-Table-ms)

# Step 2: The Morse table

**Question:** Where does the program get the dots and dashes of each character?

![Step 2: the Morse table](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/082-assignment-text-to-morse-code-converter/raw/branch/main/docs/images/step-2-morse-table.png)

## What the code does

`MORSE_CODE_DICT` in `domain/constants.py` maps **54** characters (the letters A to Z, the digits 0 to 9 and 18 punctuation marks) to their signal patterns, for example `S` to `...` and `0` to `-----`. `signal_pattern_for` looks a character up after turning it into upper case, so `s` and `S` give the same pattern.

## What you gained

- A dictionary is a lookup table: a key gives a value in one step.
- Constants live in one module (`constants.py`), written once.
- `str.upper()` makes the lookup independent of the case.

Previous: [Step-1-The-Road](Step-1-The-Road) · Next: [Step-3-Convert-Text](Step-3-Convert-Text)
