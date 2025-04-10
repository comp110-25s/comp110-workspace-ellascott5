from dictionary import invert
from dictionary import favorite_color
from dictionary import count
from dictionary import bin_len


"""Tests for dictionary functions!"""

__author__: str = "730736431"


def test_invert_normal() -> None:
    """Returns inverted function."""

    y: dict[str, str]


def test_favorite_color_normal() -> None:
    """Returns favorite color (normal behavior)"""

    x: dict[str, str] = {"A": "blue", "B": "red", "C": "red"}
    assert (favorite_color(x)) == "red"


def test_favorite_color_tie() -> None:
    """Favorite color returns first encountered color in the event of a tie."""
    x: dict[str, str] = {"A": "blue", "B": "red", "C": "red", "D": "blue", "E": "pink"}
    assert (favorite_color(x)) == "blue"


def test_favorite_color_() -> None:
    """give desc"""
    x: dict[str, str] = {"A": "blue", "B": "red", "C": "red"}
    assert (favorite_color(x)) == "none"
