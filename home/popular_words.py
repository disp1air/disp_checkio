import re
def popular_words(text: str, words: list) -> dict:
    res = {}

    for item in words:
        repeated_items_list: list = re.findall(f"^{item} | {item} | {item}$|\\n{item} | {item}\\n", text.lower())
        res[item] = len(repeated_items_list)
    return res

def popular_words(text, words):
    lower_count = text.lower().split().count
    return {word: lower_count(word) for word in words}

def popular_words(text, words):
    return dict(zip(words, map(text.lower().split().count, words)))

def popular_words(text, words):
    
    return {word:text.lower().split().count(word.lower()) for word in words}

def popular_words(text: str, words: list) -> dict:
    return {word:text.lower().split().count(word) for word in words}

def popular_words(text: str, words: list) -> dict:
    a = {}
    
    lo = text.lower()
    text = lo.split()
    
    for x in range(len(words)):
        a[words[x]] = text.count(words[x])
                
    return a

def popular_words(text: str, words: list) -> dict:
    return {i: text.lower().split().count(i) for i in words}

def popular_words(text, words):
    counter = {word: 0 for word in words}
    for word in text.lower().split():
        if word in counter:
            counter[word] += 1
    return counter

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
