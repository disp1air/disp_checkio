def most_frequent(data: list) -> str:
    """
        determines the most frequently occurring string in the sequence.
    """
    return max(set(data), key = data.count)


def most_frequent(data):
    items = dict()
    for item in data: items[item] = items[item] + 1 if item in items else 1
    return max(items, key=items.__getitem__ )


def most_frequent(data):
    max = 0
    for word in data:
        count = data.count(word)
        if count > max:
            max = count
            returned = word
    return returned


if __name__ == '__main__':
    print(most_frequent([ 'a', 'b', 'c', 'a', 'b', 'a' ]))
    assert most_frequent([ 'a', 'b', 'c', 'a', 'b', 'a' ]) == 'a'
    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
