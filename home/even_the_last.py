def even_the_last(array: list) -> int:
    """
        sums even-indexes elements and multiply at the last
    """
    res = 0

    if len(array) == 0:
        return res

    for i in array[::2]:
        res += i

    return res * array[-1]


def even_the_last(array: list) -> int:
    if not array: return 0
    return sum(array[0::2]) * array[-1]


if __name__ == '__main__':
    assert even_the_last([0, 1, 2, 3, 4, 5]) == 30
    assert even_the_last([1, 3, 5]) == 30
    assert even_the_last([6]) == 36
    assert even_the_last([]) == 0
