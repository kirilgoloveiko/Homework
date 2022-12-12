class Music:
    def __init__(self, author, name):
        self.author = author
        self.name = name

    def __str__(self):
        return None

    def __repr__(self):
        return None


class ClassicalMusic(Music):
    def __init__(self,author, name, nation):
        Music.__init__(self, author, name)
        self.nation = nation

    def __str__(self):
        return f'{self.author} - {self.name}, nation: {self.nation}'

    def __repr__(self):
        return f'{self.author}, {self.name}, {self.nation}'

    def __getattribute__(self, item):
        if item == 'nation':
            n = super().__getattribute__('nation')
            return f'nation={n}. Do you like their music?)'
        return super().__getattribute__(item)

    def acknowledge(self):
        print('Меня будут слушать и через 150 лет')

class PopularMusic(Music):
    def __init__(self, author, name, type):
        Music.__init__(self, author, name)
        self.type = type

    def __str__(self):
        return f'{self.author} - {self.name}, type: {self.type}'

    def __repr__(self):
        return f'{self.author}, {self.name}, {self.type}'

    def __getattribute__(self, item):
        if item == 'name':
            n = super().__getattribute__('name')
            return f'{n}. Do you turn on this song during a lesson?)'
        return super().__getattribute__(item)


class RegionalMusic(Music):
    def __init__(self, author, name, region):
        Music.__init__(self, author, name)
        self.region = region

    def __str__(self):
        return f'{self.author} - {self.name}, region: {self.region}'

    def __repr__(self):
        return f'{self.author}, {self.name}, {self.region}'

    def __getattribute__(self, item):
        if item == 'name':
            a = super().__getattribute__('author')
            n = super().__getattribute__('name')
            r = super().__getattribute__('region')
            return f'{a}++++{n}++++{r} 😈'
        return super().__getattribute__(item)


# ___________________________________________________________________________
class WesternClassicalMusic(ClassicalMusic):
    def __init__(self, author, name, nation, era):
        ClassicalMusic.__init__(self, author, name, nation)
        self.era = era

    def __str__(self):
        return f'{self.author} - {self.name}, nation: {self.nation}/era: {self.era}'

    def __repr__(self):
        return f'{self.author}, {self.name}, {self.nation}, {self.era}'


class RockMusic(PopularMusic, ClassicalMusic):
    def __init__(self, author, name, type, category, nation):
        PopularMusic.__init__(self, author, name, type)
        ClassicalMusic.__init__(self, author, name, nation)
        self.category = category

    def __str__(self):
        return f'Song: {self.author} - {self.name}, type: {self.type}/category: {self.category}'

    def __repr__(self):
        return f'{self.author}, {self.name}, {self.type}, {self.category}'


class LatinMusic(RegionalMusic):
    def __init__(self, author, name, region, language):
        RegionalMusic.__init__(self, author, name, region)
        self.language = language

    def __str__(self):
        return f'Song: {self.author} - {self.name}, region: {self.region}/langeage: {self.language}'

    def __repr__(self):
        return f'{self.author}, {self.name}, {self.region}, {self.language}'


classical = ClassicalMusic(author='Ludovico Einaudi', name='Nuvole Bianche', nation="Italian")
popular = PopularMusic(author='A2M', name='I Got Bitches', type='rap')
regional = RegionalMusic(author='BTS', name='FAKE LOVE', region='Asian')
west_classical = WesternClassicalMusic(author='Ludwig Van Beethoven', name='Fur Elise', nation='Germany', era='Early')
rock_music = RockMusic(author='Simple Plan', name='Take my hand', type='rock', category='alternative', nation='Canada')
latin_music = LatinMusic(author='Kaoma', name='Lambada', region='Eastern America', language='Brazilian')

