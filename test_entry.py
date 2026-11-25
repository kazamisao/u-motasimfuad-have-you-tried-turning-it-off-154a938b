"""Checks for the Have You Tried Turning It Off? entry.

Run with: python3 test_entry.py
"""

import os
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import LINE


def test_window() -> None:
    assert 1 <= len(LINE) <= 199, f"line is {len(LINE)} chars, outside 1-199"
    assert LINE.strip() == LINE and "\n" not in LINE


def test_deterministic_output() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    outputs = []
    for _ in range(2):
        with tempfile.TemporaryDirectory() as tmp:
            env = dict(os.environ, MAKEFUN_OUTPUT_DIR=tmp)
            subprocess.run(
                [sys.executable, "-P", "-s", os.path.join(here, "main.py")],
                env=env,
                check=True,
            )
            with open(os.path.join(tmp, "entry.txt"), encoding="utf-8") as fh:
                outputs.append(fh.read())
    assert outputs[0] == outputs[1] == LINE


if __name__ == "__main__":
    test_window()
    test_deterministic_output()
    print(f"ok: {len(LINE)} chars, deterministic")
