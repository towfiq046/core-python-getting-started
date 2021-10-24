"""Model for aircraft flights."""


class Flight:
    """Flight 10. Classes"""

    def __init__(self, flight_number, aircraft):
        if not flight_number[:2].isalpha():
            raise ValueError(f'No airline code in "{flight_number}"')
        if not flight_number[:2].isupper():
            raise ValueError(f'Invalid airline code "{flight_number}"')
        if not 0 <= int(flight_number[2:]) <= 9999:
            raise ValueError(f'Invalid route number "{flight_number}"')
        self._flight_number = flight_number
        self._aircraft = aircraft
        self._row_numbers, self._seat_letters = self._aircraft.get_seating_plan()
        self._seating = [None] + [{letter: None for letter in self._seat_letters} for _ in self._row_numbers]

    def allocate_seat(self, seat, passenger):
        """
        Allocates a seat to a passenger.
        :param seat: A seat designator such as '12C'
        :param passenger: The passenger name
        :return:
        """
        row_number, seat_letter = self._parse_seat(seat)
        if self._seating[row_number][seat_letter] is not None:
            raise ValueError(f'Seat {seat} already occupied')

        self._seating[row_number][seat_letter] = passenger

    def relocate_passenger(self, current_seat, new_seat):
        """
        Relocates a passenger to a different seat.
        :param current_seat: The seat where the passenger is located.
        :param new_seat: The new seat for the passenger.
        """
        current_seat_row, current_seat_letter = self._parse_seat(current_seat)
        if self._seating[current_seat_row][current_seat_letter] is None:
            raise ValueError(f'No passenger to relocate in seat {current_seat}')

        new_seat_row, new_seat_letter = self._parse_seat(new_seat)
        if self._seating[new_seat_row][new_seat_letter] is not None:
            raise ValueError(f'Seat {new_seat} already occupied')

        self._seating[new_seat_row][new_seat_letter] = self._seating[current_seat_row][current_seat_letter]
        self._seating[current_seat_row][current_seat_letter] = None

    def number_of_available_seats(self):
        """
        Returns total available seats.
        :return: Integer
        """
        return sum(
            sum(1 for s in row.values() if s is None)
            for row in self._seating
            if row is not None
        )

    def make_boarding_cards(self, card_printer):
        """
        Makes card with passenger info.
        :param card_printer: Function object
        :return:
        """
        for passenger, seat in self._passenger_seats():
            card_printer(passenger, seat, self.get_flight_number(), self.get_aircraft_model())

    def get_aircraft_model(self):
        """
        Returns aircraft model number.
        :return: String
        """
        return self._aircraft.get_model()

    def get_flight_number(self):
        """
        Returns flight number
        :return: String
        """
        return self._flight_number

    def get_airline_code(self):
        """
        Returns airline code
        :return: String
        """
        return self._flight_number[:2]

    def _parse_seat(self, seat):
        seat_letter = seat[-1]
        if seat_letter not in self._seat_letters:
            raise ValueError(f'Invalid seat letter {seat_letter}')

        row_text = seat[:-1]
        try:
            row_number = int(row_text)
        except ValueError:
            raise ValueError(f'Invalid seat row {row_text}')

        if row_number not in self._row_numbers:
            raise ValueError(f'Invalid row number {row_number}')

        return row_number, seat_letter

    def _passenger_seats(self):
        for row in self._row_numbers:
            for letter in self._seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield passenger, f'{row}{letter}'


def console_card_printer(passenger, seat, flight_number, aircraft):
    """
    Prints decorated card with passenger related info.
    :param passenger: String
    :param seat: String
    :param flight_number: String
    :param aircraft: String
    :return:
    """
    output = f'| Name: {passenger} Flight: {flight_number} Seat: {seat} Aircraft: {aircraft} |'
    banner = '+' + '-' * (len(output) - 2) + '+'
    border = '|' + ' ' * (len(output) - 2) + '|'
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()


class Aircraft:
    """Aircraft base 10. Classes"""
    def __init__(self, registration):
        self._registration = registration

    def get_registration(self):
        """
        Returns registration number
        :return: String
        """
        return self._registration

    def get_model(self):
        """
        Returns model number
        :return: String
        """
        return self._model

    def get_seat_letters(self):
        """
        Returns seating letters
        :return: String
        """
        return self._seat_letters

    def number_of_seats(self):
        """
        Calculates and returns total number of seats for a aircraft.
        :return:
        """
        rows, row_seats = self.get_seating_plan()
        return len(rows) * len(row_seats)


class AirbusA319(Aircraft):
    """Airbus A319 10. Classes"""

    def __init__(self, registration):
        super().__init__(registration)
        self._model = 'Airbus A319'
        self._seat_letters = 'ABCDEF'

    def get_seating_plan(self):
        """
        Returns number of seats and seating letters
        :return: Generator and String
        """
        return range(1, 23), self._seat_letters


class Boeing777(Aircraft):
    """Boeing777 10. Classes"""
    def __init__(self, registration):
        super().__init__(registration)
        self._model = 'Boeing 777'
        self._seat_letters = 'ABCDEFGHJK'

    def get_seating_plan(self):
        """
        Returns number of seats and seating letters
        :return: Generator and String
        """
        return range(1, 56), self._seat_letters
