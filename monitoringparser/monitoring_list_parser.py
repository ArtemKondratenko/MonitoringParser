from pathlib import Path
from collections.abc import Iterable
from typing import TextIO


def load(file: TextIO) -> set[Path]:
    return set(Path(path.strip()) for path in file)


def dump(paths: Iterable[Path], file: TextIO, existing_paths: set[Path] = None):
    if existing_paths is None:
        existing_paths = set()
    for path in paths:
        absolute_path = Path(path).absolute()
        if absolute_path not in  existing_paths:
            file.write(str(absolute_path) + "\n")
            print(f"Add path: {absolute_path}")
        else:
            print(f"The path:  {absolute_path} already exists!")
