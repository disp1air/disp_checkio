import re

def three_words(words: str) -> bool:
    # this solution distinguish situations like this:
    # "1abc df fff1" - since 1abc isn't a word it returns False;
    # otherwise it might be simplified: "[a-zA-Z]+ [a-zA-Z]+ [a-zA-Z]+"
    res: list = re.findall(
        "^[a-zA-Z]+ [a-zA-Z]+ [a-zA-Z]+ |^[a-zA-Z]+ [a-zA-Z]+ [a-zA-Z]+$|( [a-zA-Z]+){3} | [a-zA-Z]+ [a-zA-Z]+ [a-zA-Z]+$",
        words
    )
    return len(res) > 0


def three_words(words):
    succ = 0
    for word in words.split():
        succ = (succ + 1)*word.isalpha()
        if succ == 3: return True
    else: return False


def three_words(words):
    return bool(re.compile("([a-zA-Z]+ ){2}[a-zA-Z]+").search(words))


def three_words(words):
    return bool(re.search('\D+ \D+ \D+', words))


def three_words(s):
    l = [x.isalpha() for x in s.split()]
    return [True]*3 in [l[i:i+3] for i in range(len(l)-2)]


def three_words(x):
    x = x.split()
    x = ''.join([str(0) if i.isdigit() else str(1) for i in x])
    return True if "111" in x else False


def three_words(words):
    return re.search('[a-zA-Z]+ [a-zA-Z]+ [a-zA-Z]+', words) is not None


def three_words(words):
    return not re.search("\D+(\s+\D+){2}", words) is None


if __name__ == '__main__':
    assert three_words("Hello World hello") == True
    assert three_words("He is 123 man") == False
    assert three_words("1 2 3 4") == False
    assert three_words("bla bla bla bla") == True
    assert three_words("Hi") == False
