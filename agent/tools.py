import os
import subprocess
from pathlib import Path
from typing import List, Optional

from rich.console import Console
from rich.syntax import Syntax


console = Console()


def read_file(path: str, max_bytes: int = 200_000) -> str:
    file_path = Path(path)
    data = file_path.read_bytes()
    return data[:max_bytes].decode("utf-8", errors="ignore")


def write_file(path: str, content: str) -> None:
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content, encoding="utf-8")


def list_files(root: str, patterns: Optional[List[str]] = None) -> List[str]:
    base = Path(root)
    result: List[str] = []
    globs = patterns or ["**/*.py", "**/*.md", "**/*.toml", "**/*.json", "**/*.yaml", "**/*.yml"]
    for g in globs:
        for p in base.glob(g):
            if p.is_file():
                result.append(str(p))
    return sorted(result)


def run_command(cmd: str, cwd: Optional[str] = None, timeout: int = 120) -> str:
    proc = subprocess.run(
        cmd,
        shell=True,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=timeout,
        text=True,
    )
    return proc.stdout


def show_diff(original: str, updated: str, language: str = "python") -> None:
    console.rule("Proposed Edit Preview")
    console.print(Syntax(original, language, theme="monokai", line_numbers=True), justify="left")
    console.print(Syntax(updated, language, theme="monokai", line_numbers=True), justify="left")

