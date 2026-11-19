**English** · [Dansk](Step-1-The-Road-da) · [Bahasa Malaysia](Step-1-The-Road-ms)

# Step 1: The Road to Becoming a Professional Developer

**Question:** How do you start a project when nobody tells you the steps?

![Step 1: the Python version and the files of the package](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/082-assignment-text-to-morse-code-converter/raw/branch/main/docs/images/step-1-the-road.png)

## What the code does

The screenshot comes from a Docker container (Linux, Python 3.13): `python --version` and the list of the files of the package. The package has three layers: `domain` (the Morse table and its error), `application` (the use case `text_to_morse`) and `presentation` (the command line). The use case, its sequence diagram and the class diagram were written and reviewed before the first line of code; see the [use case](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/082-assignment-text-to-morse-code-converter/src/branch/main/docs/use-cases/uc-001/uc.md) and the [class diagram](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/082-assignment-text-to-morse-code-converter/src/branch/main/docs/dcd.md).

## What you gained

- Write down what the program must do (a use case) before you write code.
- Split the code into layers, so the Morse table does not depend on the command line.
- One `.venv` for each project, an editable install and tests from the start.

Previous: [Getting-Started](Getting-Started) · Next: [Step-2-Morse-Table](Step-2-Morse-Table)
