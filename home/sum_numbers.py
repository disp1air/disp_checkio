import re

def sum_numbers(text: str) -> int:
    z: str = re.findall("^\d+\s|\s\d+\s|\s\d+$", text)
    return sum([int(i.strip()) for i in z])


def sum_numbers(text: str) -> int:
    return sum(int(word) for word in text.split() if word.isdigit())


sum_numbers = lambda text: sum(int(word) for word in text.split() if word.isdigit())


def sum_numbers(text: str) -> int:
    return sum(map(int, filter(str.isdigit, text.split())))


def sum_numbers(text: str) -> int:
    return sum(int(word) for word in text.split() if word.isdigit())


def sum_numbers(text: str) -> int:

    return sum([int(i) for i in text.split() if i.isnumeric()])


if __name__ == "__main__":
    assert sum_numbers("hi") == 0
    assert sum_numbers("who is 1st here") == 0
    assert sum_numbers("my numbers is 2") == 2
    assert (
        sum_numbers(
            "This picture is an oil on canvas "
            "painting by Danish artist Anna "
            "Petersen between 1845 and 1910 year"
        )
        == 3755
    )
    assert sum_numbers("5 plus 6 is") == 11
    assert sum_numbers("") == 0
