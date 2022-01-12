def backward_string(text: str) -> str:
    return text[::-1]


if __name__ == '__main__':
    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'