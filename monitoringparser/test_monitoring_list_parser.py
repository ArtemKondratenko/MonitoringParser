import os.path
from pathlib import Path
from collections.abc import Generator
from typing import TextIO
import pytest
import tempfile
from monitoringparser.monitoring_list_parser import load, dump


@pytest.fixture
def tmpfile() -> Generator[TextIO, None]:
    with tempfile.TemporaryFile("w+") as file:
        yield file


def test_dump_and_load(tmpfile):
    dump([Path("dir1"), Path("dir2")], tmpfile, set())
    tmpfile.seek(0)
    assert load(tmpfile) == {Path("dir1").absolute(), Path("dir2").absolute()}

    dump([Path("dir3")], tmpfile, {Path("dir1").absolute(), Path("dir2").absolute()})
    tmpfile.seek(0)
    assert load(tmpfile) == {Path("dir1").absolute(), Path("dir2").absolute(), Path("dir3").absolute()}

    tmpfile.seek(0)
    dump([Path("dir4")], tmpfile)
    tmpfile.seek(0)
    assert load(tmpfile) == {Path("dir4").absolute(), Path("dir2").absolute(), Path("dir3").absolute()}


def test_(tmpfile):
    dump([Path("dir1"), Path("./dir2"), Path("/dir3")], tmpfile)
    tmpfile.seek(0)
    assert all(os.path.isabs(path) for path in load(tmpfile))
