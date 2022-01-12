def max_digit(number: int) -> int:
    s = []
    i = str(number)
    for item in i:
        s.append(item)

    return int(max(s))


def max_digit(number: int) -> int:
    return int(max(str(number)))


def max_digit(number: int) -> int:
    return max([int(i) for i in str(number)])


def max_digit(number: int) -> int:
    return int(max(list(str(number))))


if __name__ == '__main__':
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1