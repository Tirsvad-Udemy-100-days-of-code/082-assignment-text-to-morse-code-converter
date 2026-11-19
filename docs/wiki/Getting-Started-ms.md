[English](Getting-Started) · [Dansk](Getting-Started-da) · **Bahasa Malaysia**

# Bermula

Keperluan: Python 3.13 atau lebih baharu. Atur cara ini tiada kebergantungan masa jalan; `pytest`, `ruff`, `mypy`, Jupyter dan Pillow ialah alat pembangunan.

## Windows

Cipta dan gunakan `.venv` tempatan, kemas kini `pip` dan pasang projek:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Jalankan atur cara, ujian dan buku nota:

```powershell
python -m morse_converter Hello World
python -m pytest
python -m jupyter lab notebooks/Text_to_Morse_Code_Converter.ipynb
```

## Linux dan macOS

Cipta dan gunakan `.venv` tempatan, kemas kini `pip` dan pasang projek:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Jalankan atur cara, ujian dan buku nota:

```bash
python -m morse_converter Hello World
python -m pytest
python -m jupyter lab notebooks/Text_to_Morse_Code_Converter.ipynb
```

Docker hanya diperlukan untuk membuat semula tangkapan skrin (`python scripts/make_screenshots.py`); Doxygen hanya diperlukan untuk membina dokumentasi sumber (`doxygen Doxyfile`).

**Apa yang anda perolehi:** persediaan yang boleh diulang (persekitaran maya bagi setiap projek), pakej yang dipasang dalam mod boleh suntingan, dan ujian yang membuktikan hasilnya.
