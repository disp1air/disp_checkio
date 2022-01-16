import re
def popular_words(text: str, words: list) -> dict:
    res = {}

    for item in words:
        repeated_items_list: list = re.findall(f"^{item} | {item} | {item}$|\\n{item} | {item}\\n", text.lower())
        res[item] = len(repeated_items_list)
    return res

# don't forget to consider an option when using \n


popular_words("\nWhen I was One\nI had just begun\nWhen I was Two\nI was nearly new\n",
        ['i']
    )

if __name__ == '__main__':
    assert popular_words('''
        When I was One I had just begun When I was Two I was nearly new
        ''',
        ['i', 'was', 'three', 'near']
    ) == {
            'i': 4,
            'was': 3,
            'three': 0,
            'near': 0
        }
