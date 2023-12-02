from src import Game, make_games, get_possible_game_ids
import pytest


@pytest.fixture
def games():
    file = "test_data.txt"
    return list(make_games(file))


@pytest.fixture
def cubes():
    return {"red": 12, "green": 13, "blue": 14}


@pytest.fixture
def ids():
    return list(range(1, 6))


@pytest.fixture
def powers():
    return [48, 12, 1560, 630, 36]


def test_make_a_game_from_file(games):
    assert len(games) == 5


def test_all_games_have_ids(games, ids):
    for iter_id, game in enumerate(games):
        assert game.id == ids[iter_id]


def test_game_1_2_5_is_possible(games, cubes):
    assert games[0].is_possible(cubes)
    assert games[1].is_possible(cubes)
    assert games[4].is_possible(cubes)


def test_game_3_is_impossible(games, cubes):
    assert not games[2].is_possible(cubes)
    assert not games[3].is_possible(cubes)


def test_get_possible_game_ids(games, cubes):
    assert list(get_possible_game_ids(games, cubes)) == [1, 2, 5]


def test_get_game_power(games, powers):
    calc_powers = [game.get_power() for game in games]
    assert calc_powers == powers
    assert sum(calc_powers) == 2286
