**English** · [Dansk](Step-3-Convert-Text-da) · [Bahasa Malaysia](Step-3-Convert-Text-ms)

# Step 3: Convert text to Morse code

**Question:** How does a whole sentence become Morse code?

![Step 3: converting text](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/082-assignment-text-to-morse-code-converter/raw/branch/main/docs/images/step-3-convert-text.png)

## What the code does

`text_to_morse` splits the text into words with `text.split()`, joins the signal patterns of a word with one space and the words with ` / `. `SOS` gives `... --- ...` and `Hello World` gives `.... . .-.. .-.. --- / .-- --- .-. .-.. -..`. An empty or blank text gives an empty string. A character that has no pattern raises `UnsupportedCharacterError`, and nothing is converted ([ADR-0001](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/082-assignment-text-to-morse-code-converter/src/branch/main/docs/adr/adr-0001-unsupported-characters-are-rejected.md)).

## What you gained

- `str.split()` splits on any white space and drops empty parts.
- `str.join()` with a generator expression builds the result without a loop variable.
- Edge cases (empty text, extra spaces, unknown characters) are part of the design, so decide them first.

Previous: [Step-2-Morse-Table](Step-2-Morse-Table) · Next: [Step-4-Command-Line](Step-4-Command-Line)
