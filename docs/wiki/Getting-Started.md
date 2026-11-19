**English** · [Dansk](Getting-Started-da) · [Bahasa Malaysia](Getting-Started-ms)

# Getting started

Requirements: Python 3.13 or newer. The program has no runtime dependency; `pytest`, `ruff`, `mypy`, Jupyter and Pillow are development tools.

## Windows

Create and use a local `.venv`, bring `pip` up to date and install the project:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Run the program, the tests and the notebook:

```powershell
python -m morse_converter Hello World
python -m pytest
python -m jupyter lab notebooks/Text_to_Morse_Code_Converter.ipynb
```

## Linux and macOS

Create and use a local `.venv`, bring `pip` up to date and install the project:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Run the program, the tests and the notebook:

```bash
python -m morse_converter Hello World
python -m pytest
python -m jupyter lab notebooks/Text_to_Morse_Code_Converter.ipynb
```

Docker is only needed to make the screenshots again (`python scripts/make_screenshots.py`); Doxygen is only needed to build the source documentation (`doxygen Doxyfile`).

**What you gained:** a repeatable set-up (a virtual environment for each project), a package you install in editable mode, and tests that prove the results.
