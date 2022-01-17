def checkio(values: list) -> list:
    return sorted(values, key=lambda value: abs(value))


def checkio(numbers_array):
    return sorted(numbers_array, key=abs)


if __name__ == '__main__':
    assert checkio([-20, -5, 10, 15]) == [-5, 10, 15, -20]
    assert checkio([1, 2, 3, 0]) == [0, 1, 2, 3]
    assert checkio([-1, -2, -3, 0]) == [0, -1, -2, -3]
