from src import LiftConfigurator, read_file
import pytest


@pytest.fixture
def lift_configurator():
    return LiftConfigurator(read_file("test_data.txt"))


@pytest.fixture
def numbers(lift_configurator):
    return list(lift_configurator.get_numbers())


def test_get_numbers_contains_467(numbers):
    assert 467 in numbers


def test_get_numbers_contains_617(numbers):
    assert 617 in numbers


def test_get_numbers_contains_35(numbers):
    assert 35 in numbers


def test_get_numbers_contains_664(numbers):
    assert 664 in numbers


def test_get_numbers_contains_598(numbers):
    assert 598 in numbers


def test_get_numbers_does_not_contain_114(numbers):
    assert 114 not in numbers


def test_get_numbers_sum(numbers):
    print(numbers)
    assert sum(numbers) == 4361


def test_get_gears(lift_configurator):
    assert list(lift_configurator.get_gears())[0] == 16345


def test_get_gears_sum(lift_configurator):
    assert sum(lift_configurator.get_gears()) == 467835
