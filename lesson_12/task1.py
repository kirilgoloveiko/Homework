from datetime import datetime


class User:

    def __init__(self, name, surname, age: int, country, gender, profession):
        self.name = name
        self.surname = surname
        self.age = age
        self.country = country
        self.gender = gender
        self.profession = profession

    def __str__(self):
        return f'{self.name} {self.surname} ({self.gender}) is {self.age} from {self.country} - {self.profession}'

    def birth_year(self):
        current_date = datetime.date(datetime.now())
        birth_year = current_date.year - self.age
        return f'{self.name} {self.surname} was born in {birth_year}'

    def generate_email(self):
        return f'{self.name.lower()}{self.surname.lower()}@gmail.com'

    def create_doctor(self):
        name = input('Enter name: ')
        surname = input('Enter surname: ')
        age = int(input('Enter age: '))
        country = input('Enter country: ')
        gender = input('Enter gender (male/female): ')
        return User(name, surname, age, country, gender, profession='doctor')

    def create_policeman(self):
        name = input('Enter name: ')
        surname = input('Enter surname: ')
        age = int(input('Enter age: '))
        country = input('Enter country: ')
        gender = input('Enter gender (male/female): ')
        return User(name, surname, age, country, gender, profession='policeman')

    def create_teacher(self):
        name = input('Enter name: ')
        surname = input('Enter surname: ')
        age = int(input('Enter age: '))
        country = input('Enter country: ')
        gender = input('Enter gender (male/female): ')
        return User(name, surname, age, country, gender, profession='teacher')


# user1 = User(name='Kiril', surname='Goloveiko', age=25, country='Belarus', gender='male', profession='Python-developer')

