**English** · [Dansk](Step-4-Command-Line-da) · [Bahasa Malaysia](Step-4-Command-Line-ms)

# Step 4: Run it from the command line

**Question:** How does a user run the program, and how does it say that something went wrong?

![Step 4: the command line](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/082-assignment-text-to-morse-code-converter/raw/branch/main/docs/images/step-4-command-line.png)

## What the code does

`python -m morse_converter Hello World` runs `__main__.py`. The command joins the arguments with one space; with no arguments it asks for the text with `input()`. It prints the Morse code and exits with 0. For an unsupported character, such as `~`, it prints the character on the error stream and exits with 1, as the screenshot shows.

## What you gained

- `python -m package` runs the `__main__.py` of a package.
- `sys.argv` holds the arguments and `input()` reads a line.
- Exit code 0 means success; output for the user goes to standard output and errors to standard error.
- A test can run the program as a subprocess and check its output and exit code.

Previous: [Step-3-Convert-Text](Step-3-Convert-Text) · Next: [Summary](Summary)
