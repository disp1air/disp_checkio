def split_list(items: list) -> list:
    items_len = len(items)

    if items_len % 2 == 1:
        return [items[:items_len // 2 + 1], items[items_len // 2 + 1:]]
    return [items[:items_len // 2], items[items_len // 2:]]


def split_list(items: list) -> list:
    mid = (len(items) + 1) // 2
    return [items[:mid], items[mid:]]


if __name__ == '__main__':
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
