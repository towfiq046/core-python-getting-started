"""Instance Method: Functions which can be called on objects or instances of class."""


class Flight:

    # Instance method must accept a reference to the actual instance on which the method is called, it is the first
    # argument (self)
    def number(self):
        return 'SN060'


flight = Flight()

flight.number()
# No argument is provided for number
# It is syntactical sugar for Flight.number(flight).
Flight.number(flight)
