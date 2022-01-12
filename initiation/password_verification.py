def is_acceptable_password(password: str) -> bool:
    # return True if len(password) > 6 else False
    return len(password) > 6


if __name__ == '__main__':
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False