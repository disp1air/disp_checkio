from typing import Tuple


def sum_by_types(items: list) -> Tuple[str, int]:
    str_sum = ''
    int_sum = 0

    for item in items:
        if type(item) is str:
            str_sum += item
        elif type(item) is int:
            int_sum += item
    return (str_sum, int_sum)



if __name__ == "__main__":
    assert sum_by_types([]) == ("", 0)
    assert sum_by_types([1, 2, 3]) == ("", 6)
    assert sum_by_types(["1", 2, 3]) == ("1", 5)
    assert sum_by_types(["1", "2", 3]) == ("12", 3)
    assert sum_by_types(["1", "2", "3"]) == ("123", 0)
    assert sum_by_types(["size", 12, "in", 45, 0]) == ("sizein", 57)
