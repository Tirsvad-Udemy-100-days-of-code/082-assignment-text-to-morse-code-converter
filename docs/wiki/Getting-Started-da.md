[English](Getting-Started) · **Dansk** · [Bahasa Malaysia](Getting-Started-ms)

# Kom i gang

Krav: Python 3.13 eller nyere. Programmet har ingen afhængigheder ved kørsel; `pytest`, `ruff`, `mypy`, Jupyter og Pillow er udviklingsværktøjer.

## Windows

Opret og brug et lokalt `.venv`, opdatér `pip` og installér projektet:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Kør programmet, testene og notebooken:

```powershell
python -m morse_converter Hello World
python -m pytest
python -m jupyter lab notebooks/Text_to_Morse_Code_Converter.ipynb
```

## Linux og macOS

Opret og brug et lokalt `.venv`, opdatér `pip` og installér projektet:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Kør programmet, testene og notebooken:

```bash
python -m morse_converter Hello World
python -m pytest
python -m jupyter lab notebooks/Text_to_Morse_Code_Converter.ipynb
```

Docker skal kun bruges til at lave skærmbillederne igen (`python scripts/make_screenshots.py`); Doxygen skal kun bruges til at bygge kildedokumentationen (`doxygen Doxyfile`).

**Hvad du fik ud af det:** en gentagelig opsætning (et virtuelt miljø til hvert projekt), en pakke, du installerer i redigerbar tilstand, og tests, der beviser resultaterne.
