import re

def first_word(text: str) -> str:
    """
    returns the first word in a given text.
    """
    # do not forget ' symbol
    return re.search("[a-zA-Z']+", text).group()


def first_word(text):
    return text.replace(',', ' ').replace('.', ' ').split()[0]


def first_word(text):
    import re
    return re.search("[A-z']+", text)[0]


def first_word(text: str) -> str:
    return re.search("([\w']+)", text).group(1)


if __name__ == "__main__":
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
