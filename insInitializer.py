# __init__ is an initializer not a constructor.
# The purpose of __init__ is to configure an object which already exists by the time __init__ is called.
# As we don't need object attributes before we create them.

"""Model for aircraft flights."""


class Flight:
    # Class invariants: Truths about object for the lifetime.
    def __init__(self, number):
        if not number[:2].isalpha():
            raise ValueError(f'No airline code in "{number}"')
        if not number[:2].isupper():
            raise ValueError(f'Invalid airline code "{number}"')
        if not (0 <= int(number[2:]) <= 9999):
            raise ValueError(f'Invalid route number "{number}"')

        self._number = number

    # Methods are bound attributes of the object.
    # number attribute and number method will result in a name conflict.
    def get_number(self):
        return self._number

    def get_airline_code(self):
        return self._number[:2]


# Argument passed to the constructor is forwarded to the initializer.
flight = Flight('SN010')
