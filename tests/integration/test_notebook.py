"""@file test_notebook.py
@brief Runs the notebook headlessly so that it cannot rot (needs no GUI).
"""

from pathlib import Path

import nbformat
from nbclient import NotebookClient

NOTEBOOK = (
    Path(__file__).resolve().parents[2]
    / "notebooks"
    / "Text_to_Morse_Code_Converter.ipynb"
)


def test_notebook_runs_from_top_to_bottom() -> None:
    notebook = nbformat.read(NOTEBOOK, as_version=4)
    NotebookClient(notebook, timeout=120, kernel_name="python3").execute()
    outputs = [
        output.get("text", "")
        for cell in notebook.cells
        if cell.cell_type == "code"
        for output in cell.outputs
    ]
    joined = "".join(outputs)
    assert "... --- ..." in joined
    assert ".... . .-.. .-.. --- / .-- --- .-. .-.. -.." in joined
    assert "Not supported: '~'" in joined
