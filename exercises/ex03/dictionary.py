"""Learning to use dictionaries!"""

__author__: str = "730736431"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts a dictionary."""

    temps: dict[str, str] = dict()
    for key in input:
        value = input[key]
        if value in temps:
            raise KeyError("Duplicate value")
        temps[value] = key
    return temps


def count(number: list[str]) -> dict[str, int]:
    """Counts a list."""

    thing: dict[str, int] = {}
    for key in number:
        if key in thing:
            thing[key] += 1
        else:
            thing[key] = 1
    return thing


def favorite_color(color_dict: dict[str, str]) -> str:
    """Finds the most popular color."""

    color_name: list[str] = []

    for key in color_dict:
        color_name.append(color_dict[key])
    amount = count(color_name)
    color_value: list[int] = []
    for key in amount:
        color_value.append(amount[key])

    most_picked_color: int = max(color_value)
    for key in amount:
        if amount[key] == most_picked_color:
            return key


def bin_len(length: dict[int, set]):
    """Finds length."""
    the_length: dict[str, int] = {}
    for something in the_length:
        length = len(key)
        if length not in the_length:
            the_length[length] = set()
        the_length[length].append(something)
