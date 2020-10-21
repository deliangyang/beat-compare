import re

reg_replace = re.compile(r'(#|\?|\||\x20|\s|\t|-|\'|"|/| /|\(|\)|（|）|\.|_)')

reg_dot_zero = re.compile(r'\.0$')

__map = {
    'Ｈ': 'H',
    'Ａ': 'A',
    'Ｂ': 'B',
    'Ｃ': 'C',
    'Ｐ': 'P',
    'Ｙ': 'Y',
    'Ｉ': 'I',
    'Ｒ': 'R',
    'Ｔ': 'T',
    'Ｄ': 'D',
    'Ｏ': 'O',
    'Ｕ': 'U',
    'Ｎ': 'N',
    'Ｅ': 'E',
    'Ｆ': 'F',
    'Ｍ': 'M',
    'Ｓ': 'S',
    'Ｇ': 'G',
    'Ｌ': 'L',
    'Ｗ': 'W',
    'Ｋ': 'K',
    'Ｖ': 'V',
    'Ｊ': 'J',
    'Ｘ': 'X',
    'Ｚ': 'Z',
    'Ｑ': 'Q',
}


def __char_replace(s):
    for k, v in __map.items():
        s = str(s).replace(k, v)
    return s


def replace(s):
    return __char_replace(reg_replace.sub('', str(s).lower()))


def replace_dot_zero(s, s2):
    if len(str(s)) <= 0:
        s = str(s2)
    return reg_dot_zero.sub('', str(s))
