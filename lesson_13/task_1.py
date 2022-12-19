from bs4 import BeautifulSoup
import requests

url = 'https://myfin.by'
request = requests.get(url)
soup = BeautifulSoup(request.text, 'html.parser')

current_dollar_exchange_reat = soup.find('input', id='to_input_curr').get('value')
# print(current_dollar_exchange_reat)


class Car:
    counter = 0

    def __init__(self, mark: str, year: int, mileage: float, price: int):
        self.mark = mark
        self.year = year
        self._mileage = mileage
        self.price = price
        Car.counter += 1

    def __str__(self):
        return f'Car {self.mark}, {self.year} with mileage {self.mileage} costs {self.price}'

    def __eq__(self, other):
        return (self.mark == other.mark and
                self.year == other.year)

    def get_price_in_dollars(self):
        return f'Price is {self.price * float(current_dollar_exchange_reat)}$'

    @classmethod
    def get_count(cls):
        return cls.counter

    @staticmethod
    def get_country(mark: str):
        if mark.capitalize() in ['BMW', 'Volkswagen', 'Mercedes-Benz', 'Audi', 'Porsche']:
            country = 'Germany'
        elif mark.capitalize() in ['Ferrari', 'Lamborghini', 'Maserati', 'Fiat', 'Alfa Romeo']:
            country = 'Italy'
        elif mark.capitalize() in ['Peugeot', 'Citroen', 'Renault']:
            country = 'France'
        elif mark.capitalize() in ['Chevrolet', 'Buick', 'GMC', 'Cadillac', 'Ford', 'Chrysler']:
            country = 'The USA'
        else:
            country = 'Unknown country'
        return f'The car "{mark}" from {country}'

    @property
    def mileage(self):
        return f'{self.mark}: mileage is {self._mileage}'

    @mileage.setter
    def mileage(self, mileage):
        self._mileage = mileage

    @mileage.deleter
    def mileage(self):
        del self._mileage


class ElectricCar(Car):

    def __init__(self, mark: str, year: int, mileage: float, price: int, power_reserve: int):
        Car.__init__(self, mark, year, mileage, price)
        self.power_reserve = power_reserve

    @staticmethod
    def get_country(mark: str):
        return 'Do you want such a car? Learn PYTHON!'






