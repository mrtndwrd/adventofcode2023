import re, math


def read_file(filename):
    with open(filename, "r") as file_content:
        lines = file_content.readlines()
    return lines


class LiftConfigurator:
    def __init__(self, lines):
        self.lines = lines
        # Line index, char index and value of used numbers
        self.used_numbers: set(tuple[int, int, str]) = set()

    def _get_relevant_line_ixes(self, line_ix):
        return (max(line_ix - 1, 0), min(line_ix + 2, len(self.lines)))

    @staticmethod
    def _is_symbol(char):
        return bool(re.search("[^0-9.\n]", char))

    @staticmethod
    def _is_gear(char):
        return char == "*"

    def search_numbers(self, char_ix, symbol_line_ix):
        for line_ix in range(*self._get_relevant_line_ixes(symbol_line_ix)):
            line = self.lines[line_ix]
            for match in re.finditer("[0-9]+", line):
                identifier = (line_ix, match.start(), match[0])
                if (
                    match.start() - 1 <= char_ix <= match.end()
                    and identifier not in self.used_numbers
                ):
                    yield int(match[0])
                    self.used_numbers.add(identifier)

    def get_numbers(self):
        for line_ix, line in enumerate(self.lines):
            for char_ix, char in enumerate(line):
                if self._is_symbol(char):
                    for number in list(self.search_numbers(char_ix, line_ix)):
                        yield number

    def get_gears(self):
        for line_ix, line in enumerate(self.lines):
            for char_ix, char in enumerate(line):
                if self._is_gear(char):
                    numbers = list(self.search_numbers(char_ix, line_ix))
                    if len(numbers) > 1:
                        yield math.prod(numbers)


if __name__ == "__main__":
    file = "real_data.txt"
    lift_configurator = LiftConfigurator(read_file(file))
    numbers = lift_configurator.get_numbers()
    # Star 1
    print(sum(numbers))

    lift_configurator = LiftConfigurator(read_file(file))
    # Star 2
    print(sum(lift_configurator.get_gears()))
