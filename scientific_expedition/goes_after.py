def goes_after(word: str, first: str, second: str) -> bool:
    """
    In a given word you need to check if one symbol goes only right after another.

    Cases you should expect while solving this challenge:

    If more than one symbol is in the list you should always count the first one
    one of the symbols are not in the given word - your function should return False;
    any symbol appears in a word more than once - use only the first one;
    two symbols are the same - your function should return False;
    the condition is case sensitive, which means 'a' and 'A' are two different symbols.
    """
    if first not in word or second not in word or first == second:
        return False
    return word.index(second) == word.index(first) + 1


def goes_after(word: str, first: str, second: str) -> bool:
    try:
        return word.index(second)-word.index(first) == 1
    except ValueError:
        return False


def goes_after(word: str, first: str, second: str) -> bool:
    return word.find(second) - word.find(first) == 1


if __name__ == "__main__":
    assert goes_after("world", "w", "o") == True
    assert goes_after("world", "w", "r") == False
    assert goes_after("world", "l", "o") == False
    assert goes_after("panorama", "a", "n") == True
    assert goes_after("list", "l", "o") == False
    assert goes_after("", "l", "o") == False
    assert goes_after("list", "l", "l") == False
    assert goes_after("world", "d", "w") == False
    assert goes_after("transport", "r", "t") == False
