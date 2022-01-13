def split_list(items: list) -> list:
    mid = len(items) // 2
    return [items[:mid], items[mid:]]


if __name__ == '__main__':
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1], [2, 3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2], [3, 4, 5]]
    assert split_list([1]) == [[], [1]]
    assert split_list([]) == [[], []]
