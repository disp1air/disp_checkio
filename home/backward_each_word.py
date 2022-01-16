def backward_string_by_word(text: str) -> str:
    # your code here
    # separate in a list by space, 
    # this will create empty elements where multiple spaces
    # reverse every word
    # and reconstitute the sentence by joining words with a space separation
    return ' '.join(word[::-1] for word in text.split(' '))


def backward_string_by_word(text: str) -> str:
    return ' '.join([word[::-1] for word in text.split(' ')])


# !!!
def backward_string_by_word(text: str) -> str:
    for i in text.split():
        print(i)
        text = text.replace(i,i[::-1])    
    return text


if __name__ == '__main__':
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
