from pathlib import Path
from collections.abc import Iterable
from typing import TextIO

def read_existing_paths(file_path: Path) -> set:
    """Читает существующие пути из файла и возвращает их в виде множества."""
    if file_path.exists():
        with open(file_path, 'r') as file:
            return set(file.read().strip().splitlines())
    return set()

def dump(file_path: Path, paths: Iterable[Path]):
    """Записывает уникальные пути в файл."""
    existing_paths = read_existing_paths(file_path)
    with open(file_path, 'a') as file:
        for path in paths:
            absolute_path = Path(path).absolute()
            if str(absolute_path) not in existing_paths:
                file.write(str(absolute_path) + "\n")
                print(f"Added: {absolute_path}")
            else:
                print(f"Already exists: {absolute_path}")

