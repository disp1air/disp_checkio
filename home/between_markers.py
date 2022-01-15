from dataclasses import replace
import re

def between_markers(text: str, begin: str, end: str) -> str:
    """
        You are given a string and two markers (the initial and final).
        You have to find a substring enclosed between these two markers.
        But there are a few important conditions:
            The initial and final markers are always different.
            If there is no initial marker, then the first character should be considered the beginning of a string.
            If there is no final marker, then the last character should be considered the ending of a string.
            If the initial and final markers are missing then simply return the whole string.
            If the final marker comes before the initial marker, then return an empty string.
    """
    if begin not in text and end not in text:
        return text
    elif begin not in text:
        end1 = end.replace('[','\[').replace('/','\/')
        res: str = re.search(f".+{end1}", text).group()
        if res:
            return res.replace(f'{end}', '')
        return ''
    elif end not in text:
        begin1 = begin.replace('[','\[').replace('/','\/')
        res: str = re.search(f"{begin1}.+$", text).group()
        if res:
            return res.replace(f'{begin}', '')
        return ''
    elif text.index(begin) > text.index(end):
        return ''
    else:
        res: str = re.search(f"{begin}.+{end}", text).group()
        return res.replace(f'{begin}', '').replace(f'{end}', '')


def between_markers(text: str, begin: str, end: str) -> str:
    # Find i_begin
    try:
        i_begin = text.index(begin) + len(begin)
    except ValueError:
        i_begin = None

    # Find i_end
    try:
        i_end = text.index(end)
    except ValueError:
        i_end = None

    # Return value between markers
    return text[i_begin:i_end]


def between_markers(text: str, begin: str, end: str) -> str:
    start = text.find(begin) + len(begin) if begin in text else None
    stop = text.find(end) if end in text else None
    return text[start:stop]


if __name__ == '__main__':
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
