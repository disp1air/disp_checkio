from typing import Iterable

def replace_first(items: list) -> Iterable:
    if len(items) == 0 or len(items) == 1:
        return items

    res = items[1:]
    res.append(items[0])
    return res


def replace_first(items: list) -> Iterable:
    if items:
        head, *items = items
        items = [*items, head]
    return items


def replace_first(items: list) -> Iterable:
    return items[1:] + items[:1]
    

def replace_first(items: list):
    return items[1:] + [items[0]] if items else items


def replace_first(items: list) -> list:
    if items:
        items.append(items.pop(0))
    return items


if __name__ == "__main__":
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []