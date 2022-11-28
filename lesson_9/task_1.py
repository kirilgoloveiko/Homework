class Car:

    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def __str__(self):
        return f'color is "{self.color}", type is "{self.type}", year is "{self.year}"'

    def turn_on_the_engine(self):
        return f'The car is on'

    def turn_off_the_engine(self):
        return f'The car is off'

