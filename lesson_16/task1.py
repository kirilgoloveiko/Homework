class Cat:
    def __init__(self, name: str):
        self.name = name
        self.counter = 0

    def to_answer(self):
        self.counter += 1
        if self.counter % 2 != 0:
            print('moore..')
        else:
            print('meow..')

    def moore(self):
        count_odd = 0
        for i in range(1, self.counter + 1):
            if i % 2 != 0:
                count_odd += 1
        return f"Метод 'moore' был вызван {count_odd} раз"

    def meow(self):
        count_even = 0
        for i in range(1, self.counter + 1):
            if i % 2 == 0:
                count_even += 1
        return f"Метод 'meow' был вызван {count_even} раз"


# cat = Cat('Babe')
