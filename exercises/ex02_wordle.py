"""A game of Wordle!"""

__author__: str = "730736431"


def contains_char(word: str, guess: str) -> bool:
    """Checks if a word has a specific character."""
    assert len(guess) == 1, f"len('{guess}') != 1"

    idx = 0
    while idx < len(word):
        if word[idx] == guess:
            return True
        else:
            idx += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Applies colorful emojis after makikng a guess."""
    assert len(guess) == len(secret), "Guess must be same length as secret."

    colors: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    idx = 0
    while idx < len(guess):
        if guess[idx] == secret[idx]:
            colors += GREEN_BOX
        elif contains_char(secret, guess[idx]):
            colors += YELLOW_BOX
        else:
            colors += WHITE_BOX
        idx += 1
    return colors


def input_guess(length: int) -> str:
    """Applies length to guess."""
    secret = input(f"Enter a {length} character word.")
    while len(secret) != length:
        secret = input(f"That wasn't {length} chars! Try again.)")
    return secret


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""

    turn: int = 1
    guess: str = ""
    while turn <= 6:
        print(f"===Turn {turn}/6===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            return
        else:
            turn += 1
    print("X/6 - Sorry, try again tomorrow!")
    return


if __name__ == "__main__":
    main(secret="codes")
