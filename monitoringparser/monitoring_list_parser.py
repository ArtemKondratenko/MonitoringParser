from pathlib import Path
from collections.abc import Iterable
from typing import TextIO


def load(file: TextIO) -> set[Path]:
    return set(Path(path.strip()) for path in file)


def dump(paths: Iterable[Path], file: TextIO):
    for path in paths:
        absolute_path = Path(path).absolute()
        file.write(str(absolute_path) + "\n")
