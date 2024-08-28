from pathlib import Path
from collections.abc import Iterable
from typing import TextIO


def load(file: TextIO) -> set[Path]:
    return set(Path(path.strip()) for path in file)


def dump(file_path: Path, paths: Iterable[Path]):
    with open(file_path, 'a') as file:
        for path in paths:
            absolute_path = Path(path).absolute()
            file.write(str(absolute_path) + "\n")
