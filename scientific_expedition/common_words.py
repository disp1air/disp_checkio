def common_words(line1: str, line2: str) -> str:
    # The result must be represented as a string of words separated by commas in alphabetic order.
    line1_list: list = line1.split(',')
    line2_list: list = line2.split(',')

    res_list: list = [item for item in line1_list if item in line2_list]
    return ','.join(sorted(res_list))


if __name__ == '__main__':
    assert common_words('hello,world', 'hello,earth') == 'hello'
    assert common_words('one,two,three', 'four,five,six') == ''
    assert common_words('one,two,three', 'four,five,one,two,six,three') == 'one,three,two'
