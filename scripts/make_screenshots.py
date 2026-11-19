"""Make one screenshot per step of the program's own output.

Each step runs a command in a Docker container (Linux, Python 3.13, no desktop;
see framework/process/gui-testing.md), saves the text it prints under results/ and
draws it as a terminal-like PNG in docs/images/. Nothing starts on the desktop of
the host, and no screenshot of the lecture is used.

Usage:
    python scripts/make_screenshots.py [output_dir]
"""

import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "images"
RESULTS = ROOT / "results"
IMAGE = "python:3.13-slim"
WIDTH = 1000
MARGIN = 24
FONT_SIZE = 20
LINE_HEIGHT = 28
BACKGROUND = "#1e1e2e"
TITLE_BAR = "#313244"
TITLE_COLOR = "#cdd6f4"
COMMAND_COLOR = "#a6e3a1"
OUTPUT_COLOR = "#f5f5f5"
FONT_FILES = (
    "consola.ttf",
    "DejaVuSansMono.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
    "Menlo.ttc",
)


@dataclass(frozen=True)
class Step:
    """One lecture step: the image file, its title and the command that shows it."""

    file: str
    title: str
    commands: tuple[str, ...]


STEPS = (
    Step(
        "step-1-the-road.png",
        "Step 1: The Road to Becoming a Professional Developer",
        ("python --version", "find src -name '*.py' | sort"),
    ),
    Step(
        "step-2-morse-table.png",
        "Step 2: The Morse table",
        (
            'python -c "'
            "from morse_converter import MORSE_CODE_DICT\n"
            "print(len(MORSE_CODE_DICT), 'characters')\n"
            "for char in 'ESOT019?':\n"
            "    print(char, MORSE_CODE_DICT[char])\n"
            '"',
        ),
    ),
    Step(
        "step-3-convert-text.png",
        "Step 3: Convert text to Morse code",
        (
            'python -c "'
            "from morse_converter import text_to_morse\n"
            "print(text_to_morse('SOS'))\n"
            "print(text_to_morse('Hello World'))\n"
            "print(repr(text_to_morse('')))\n"
            '"',
        ),
    ),
    Step(
        "step-4-command-line.png",
        "Step 4: Run it from the command line",
        (
            "python -m morse_converter Hello World",
            "python -m morse_converter good '~' text; echo exit code: $?",
        ),
    ),
)


def run_in_container(commands: tuple[str, ...]) -> str:
    """Run shell commands in a throw-away container and return what they printed."""
    docker = [
        "docker",
        "run",
        "--rm",
        "-v",
        f"{ROOT}:/work:ro",
        "-w",
        "/work",
        "-e",
        "PYTHONPATH=src",
        "-e",
        "PYTHONDONTWRITEBYTECODE=1",
        IMAGE,
        "sh",
        "-c",
        f"({chr(10).join(commands)}) 2>&1",
    ]
    done = subprocess.run(docker, capture_output=True, text=True, check=False)
    return done.stdout.replace("\r\n", "\n").rstrip("\n")


def load_font() -> ImageFont.FreeTypeFont:
    """Return the first monospaced font that this machine has."""
    for name in FONT_FILES:
        try:
            return ImageFont.truetype(name, FONT_SIZE)
        except OSError:
            continue
    raise SystemExit("No monospaced font found; install DejaVu Sans Mono.")


def render(step: Step, output: str, target: Path) -> None:
    """Draw the title bar, the command with a prompt and its output as a PNG."""
    command_lines = [
        ("$ " if index == 0 else "  ") + line
        for command in step.commands
        for index, line in enumerate(command.splitlines())
    ]
    output_lines = output.splitlines()
    rows = len(command_lines) + len(output_lines)
    height = 56 + MARGIN * 2 + rows * LINE_HEIGHT
    image = Image.new("RGB", (WIDTH, height), BACKGROUND)
    draw = ImageDraw.Draw(image)
    font = load_font()
    draw.rectangle((0, 0, WIDTH, 56), fill=TITLE_BAR)
    draw.text((MARGIN, 14), step.title, fill=TITLE_COLOR, font=font)
    y = 56 + MARGIN
    for line in command_lines:
        draw.text((MARGIN, y), line, fill=COMMAND_COLOR, font=font)
        y += LINE_HEIGHT
    for line in output_lines:
        draw.text((MARGIN, y), line, fill=OUTPUT_COLOR, font=font)
        y += LINE_HEIGHT
    target.parent.mkdir(parents=True, exist_ok=True)
    image.save(target)


def main(out_dir: Path) -> None:
    """Run every step in the container, save its text and write its image."""
    RESULTS.mkdir(exist_ok=True)
    for step in STEPS:
        output = run_in_container(step.commands)
        (RESULTS / f"{Path(step.file).stem}.txt").write_text(
            output + "\n", encoding="utf-8", newline="\n"
        )
        render(step, output, out_dir / step.file)
        print(f"wrote {out_dir / step.file}")


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUT)
