"""Introducing user input and named constants!"""

SECRET: str = "punk"


def guess_secret(word: str, secret: str, idx: int = 0) -> bool:
    pass  # TODO 1: If word and secret are different lengths, they clearly arent the same word! In this case, print "Words are different lengths." and return False
    if len(word) != len(secret):
        print("Words are different lengths.")
        return False
    # (If we reach this point, we know the words are the same length.)
    # TODO 2: If we have more letters to check...
    if idx < len(word):
        # Check to see if the next patir of letters are the same! If not, print "<letter> isnt the secret word's next letter." and return False. Otherwise, print "<letter> is at index <the index> for both words! Checking next letters..." and call the function again, moving on to the next letter in each word.
        if word[idx] != secret[idx]:
            print(f"{word[idx]} isn't the secret word's next letter.")
            return False
        else:
            print(
                f" {word[idx]} is at index {idx} for both words! Checking next letters..."
            )

            return guess_secret(word=word, secret=secret, idx=idx + 1)

    # TODO 3: If every pair of letters has been the same and there are no letters left to check, print "They are the same word!" and return True
    print("They are the same word!")
    return True
