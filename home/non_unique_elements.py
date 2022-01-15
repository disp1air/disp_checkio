def checkio(data: list) -> list:
    res = []

    for item in data:
        if data.count(item) != 1:
            res.append(item)

    return res


def checkio(data: list) -> list:
    return [item for item in data if data.count(item) != 1]


if __name__ == "__main__":
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3]
    assert list(checkio([1, 2, 3, 4, 5])) == []
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5]
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9]
