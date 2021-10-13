def nth_root(number, root):
    return number ** (1/root)


def ordinal_suffix(number):
    if number % 100 == 11:
        return 'th'
    elif number % 100 == 12:
        return 'th'
    elif number % 100 == 13:
        return 'th'
    elif number % 10 == 1:
        return 'st'
    elif number % 10 == 2:
        return 'nd'
    elif number % 10 == 3:
        return 'rd'
    return 'th'


def display_nth_root(number=1, root=1):
    return f'The {root}{ordinal_suffix(root)} root of {number} is {nth_root(number, root)}'


print(display_nth_root(27, 1388))
