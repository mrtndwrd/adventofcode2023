NUMBER_MAP = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0,
}


def read_file(file):
    with open(file) as f:
        lines = f.readlines()
    return lines


def get_first(line, rev=False) -> int:
    while line:
        if line[0].isnumeric():
            return int(line[0])
        for number_str, number_int in NUMBER_MAP.items():
            if rev:
                number_str = number_str[::-1]
            if line.startswith(number_str):
                return number_int
        line = line[1:]


def get_last(line) -> int:
    return get_first(line[::-1], rev=True)


def get_combined(line) -> int:
    return int(f"{get_first(line)}{get_last(line)}")


def get_total(file):
    return sum((get_combined(line) for line in file))


if __name__ == "__main__":
    print(get_total(read_file("file.txt")))
