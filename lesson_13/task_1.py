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
        self.mileage = mileage
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
    def miles(self):
        return f'{self.mark}: mileage is {self.mileage}'

    @miles.setter
    def miles(self, new_mileage):
        self.mileage = new_mileage

    @miles.deleter
    def miles(self):
        del self.mileage

car1 = Car('AUDI', 2018, 140_013.5, 25000)
car2 = Car('Lamba', 2019, 5000.5, 125000)

print(car1.get_count())

class ElectricCar(Car):
    counter = 0

    def __init__(self, mark: str, year: int, mileage: float, price: int, power_reserve: int):
        super().__init__(mark, year, mileage, price)
        self.power_reserve = power_reserve

    @staticmethod
    def get_country(mark: str):
        return 'Do you want such a car? Learn PYTHON!'


e_car = ElectricCar('Tesla', 2019, 10_098.5, 65000, 500)
print(ElectricCar.get_count())




