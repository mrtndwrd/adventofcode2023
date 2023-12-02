import re
from typing import Iterable
import math


class Game:
    def __init__(self, line):
        self.id = self._parse_id(line)
        self.line = line

    @staticmethod
    def _parse_id(line):
        match = re.search("Game ([0-9]+)", line)
        if match:
            return int(match.group(1))

    def get_power(self):
        cubes = [self._get_max_of_color(color) for color in ["red", "green", "blue"]]
        return math.prod(cubes)

    def _get_max_of_color(self, color):
        matches = re.findall(f"([0-9]+) {color}", self.line)
        return max([int(match) for match in matches])

    def is_possible(self, cubes):
        return all(
            [
                self._get_max_of_color(color) <= no_cubes
                for color, no_cubes in cubes.items()
            ]
        )


def make_games(filename):
    with open(filename, "r") as file_content:
        for line in file_content.readlines():
            yield Game(line)


def get_possible_game_ids(games: list[Game], cubes: dict[str, int]) -> Iterable[int]:
    for game in games:
        if game.is_possible(cubes):
            yield game.id


if __name__ == "__main__":
    filename = "real_data.txt"
    games = list(make_games(filename))
    cubes = {"red": 12, "green": 13, "blue": 14}
    print("First star:")
    print(sum(get_possible_game_ids(games, cubes)))

    print("Second star:")
    print(sum((game.get_power() for game in games)))
