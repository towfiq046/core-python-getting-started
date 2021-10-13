import sys
from math import log

DIGIT_MAP = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'zero': 0
}


def convert_string_to_digit(text):
    """
    Convert string to digit
    :param text: Iterable object
    :return: Converted string to a integer
    """
    number = ''
    try:
        for token in text:
            number += DIGIT_MAP[token]
        return int(number)
    except (KeyError, TypeError) as e:
        print(f'Conversion error: {e!r}', file=sys.stderr)
        raise


def string_log(text):
    return log(convert_string_to_digit(text))


# print(convert_string_to_digit('345'))
print(string_log(345))
