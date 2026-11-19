"""@file test_command_line.py
@brief Runs `python -m morse_converter` as a subprocess (UC-001 scenarios).
"""

import subprocess
import sys


def run_program(*arguments: str, stdin: str = "") -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "morse_converter", *arguments],
        input=stdin,
        capture_output=True,
        text=True,
        check=False,
    )


def test_main_scenario_with_arguments() -> None:
    result = run_program("Hello", "World")
    assert result.returncode == 0
    assert result.stdout == ".... . .-.. .-.. --- / .-- --- .-. .-.. -..\n"
    assert result.stderr == ""


def test_main_scenario_with_a_prompt() -> None:
    result = run_program(stdin="SOS\n")
    assert result.returncode == 0
    assert result.stdout.endswith("... --- ...\n")
    assert "Text to convert: " in result.stdout


def test_empty_text_gives_an_empty_line_and_success() -> None:
    result = run_program(stdin="\n")
    assert result.returncode == 0
    assert result.stdout.endswith("\n")
    assert result.stdout.removeprefix("Text to convert: ").strip() == ""


def test_exception_flow_2a_unsupported_character() -> None:
    result = run_program("good", "~", "text")
    assert result.returncode == 1
    assert result.stdout == ""
    assert "'~'" in result.stderr
