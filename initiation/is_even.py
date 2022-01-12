def is_even(num: int) -> bool:
    return num % 2 == 0


def is_even(num: int) -> bool:
    return not num % 2


if __name__ == '__main__':
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(0) == True
