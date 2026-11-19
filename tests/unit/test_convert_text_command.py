"""@file test_convert_text_command.py
@brief Tests of ConvertTextCommand (run, read_text, main).
"""

import sys

import pytest

from morse_converter.presentation.commands import convert_text_command
from morse_converter.presentation.constants import EXIT_ERROR, EXIT_OK


def test_read_text_joins_the_arguments_by_one_space() -> None:
    assert convert_text_command.read_text(["Hello", "World"]) == "Hello World"


def test_read_text_prompts_when_there_are_no_arguments(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    prompts: list[str] = []

    def fake_input(prompt: str) -> str:
        prompts.append(prompt)
        return "sos"

    monkeypatch.setattr("builtins.input", fake_input)
    assert convert_text_command.read_text([]) == "sos"
    assert prompts == ["Text to convert: "]


def test_run_prints_the_morse_code(capsys: pytest.CaptureFixture[str]) -> None:
    assert convert_text_command.run(["SOS"]) == EXIT_OK
    captured = capsys.readouterr()
    assert captured.out == "... --- ...\n"
    assert captured.err == ""


def test_run_names_an_unsupported_character_on_the_error_stream(
    capsys: pytest.CaptureFixture[str],
) -> None:
    assert convert_text_command.run(["a~"]) == EXIT_ERROR
    captured = capsys.readouterr()
    assert captured.out == ""
    assert "'~'" in captured.err


def test_main_passes_the_program_arguments(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr(sys, "argv", ["morse-converter", "e", "t"])
    assert convert_text_command.main() == EXIT_OK
    assert capsys.readouterr().out == ". / -\n"
