from src import read_file, get_first, get_last, get_combined, get_total
import pytest


@pytest.fixture
def file():
    return read_file("test.txt")

@pytest.fixture
def values():
    return [12, 38, 15, 77, 29, 83, 13, 24, 42, 14, 76]

def test_can_read_file(file):
    assert file

def test_read_file_returns_lines(file, values):
    assert len(file) <= len(values)

def test_get_first_int(file, values):
    assert get_first(file[0]) == values[0] // 10

def test_get_last_int(file, values):
    assert get_last(file[0]) == values[0] % 10

def test_get_combined(file, values):
    for i, line in enumerate(file):
        assert get_combined(line) == values[i]

def test_get_total(file, values):
    assert get_total(file) == sum(values)
