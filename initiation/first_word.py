def first_word(text: str) -> str:
    """
    returns the first word in a given text.
    """
    res = ''

    for i in text:
        if i == ' ':
            break
        res += i

    return res

if __name__ == "__main__":
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"