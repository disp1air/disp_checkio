import re
from timeit import timeit

def count_digits1(text: str) -> int:
    res = 0
    for i in text:
        try:
            int(i)
            res += 1
        except ValueError:
            continue
    return res


def count_digits2(text):
    return len(re.findall(r"\d", text))


def count_digits3(text):
    return len([a for a in text if a.isnumeric()])


def count_digits4(text: str) -> int:
    return sum([1 for c in text if c.isdigit()])


def count_digits5(text: str) -> int:
    return sum(map(str.isdigit, text))


print(timeit(
    'count_digits1(text)',
    setup='text = "a1sd4f 7we0"*100',
    number=10000,
    globals=globals()
))
print(timeit(
    'count_digits2(text)',
    setup='text = "a1sd4f 7we0"*100',
    number=10000,
    globals=globals()
))
print(timeit(
    'count_digits3(text)',
    setup='text = "a1sd4f 7we0"*100',
    number=10000,
    globals=globals()
))
print(timeit(
    'count_digits4(text)',
    setup='text = "a1sd4f 7we0"*100',
    number=10000,
    globals=globals()
))
print(timeit(
    'count_digits5(text)',
    setup='text = "a1sd4f 7we0"*100',
    number=10000,
    globals=globals()
))


if __name__ == '__main__':
    assert count_digits1('hi') == 0
    assert count_digits1('who is 1st here') == 1
    assert count_digits1('my numbers is 2') == 1
    assert count_digits1('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 8
    assert count_digits1('5 plus 6 is') == 2
    assert count_digits1('') == 0
