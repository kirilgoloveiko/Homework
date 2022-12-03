class Music:
    def __init__(self, author, name):
        self.author = author
        self.name = name

    def __str__(self):
        return None


''' NATION: - Andalusian
            - Indian
            - Korean
            - Persian
            - Western '''
class ClassicalMusic(Music):
    def __init__(self,author, name, nation):
        Music.__init__(self, author, name)
        self.nation = nation

    def __str__(self):
        return f'{self.author} - {self.name}, nation: {self.nation}'


''' TYPE: - blues
          - pop
          - rock
          - R&B 
          - metal
          - electronic
          - hip-hop
          - jazz
          - punk '''
class PopularMusic(Music):
    def __init__(self, author, name, type):
        Music.__init__(self, author, name)
        self.type = type

    def __str__(self):
        return f'{self.author} - {self.name}, type: {self.type}'


''' REGION: - African
            - Eastern Europe
            - Asian
            - Latin
            - Caribbean and Caribbean-influenced '''
class RegionalMusic(Music):
    def __init__(self, author, name, region):
        Music.__init__(self, author, name)
        self.region = region

    def __str__(self):
        return f'{self.author} - {self.name}, region: {self.region}'


# ___________________________________________________________________________
''' ERA: - early music
         - 20th and 21st-centuries classical music (1901–present) '''
class WesternClassicalMusic(ClassicalMusic):
    def __init__(self, author, name, nation, era):
        ClassicalMusic.__init__(self, author, name, nation)
        self.era = era

    def __str__(self):
        return f'{self.author} - {self.name}, nation: {self.nation}/era: {self.era}'

    def __repr__(self):
        return f'author={self.author}, name={self.name}, nation={self.nation}, era={self.era}'


''' CATEGORY: - alternative-rock
              - classical-rock
              - blues-rock
              - country-rock
              - experimental-rock
              - garage-rock
              - pop-rock
              - heavy-metal
              - instrumental-rock and etc.'''
class RockMusic(PopularMusic):
    def __init__(self, author, name, type, category):
        PopularMusic.__init__(self, author, name, type)
        self.category = category

    def __str__(self):
        return f'Song: {self.author} - {self.name}, type: {self.type}/category: {self.category}'

    def __repr__(self):
        return f'author={self.author}, name={self.name}, type={self.type}, category={self.category}'


''' LANGUAGE: - Brazilian
              - Hispanic '''
class LatinMusic(RegionalMusic):
    def __init__(self, author, name, region, language):
        RegionalMusic.__init__(self, author, name, region)
        self.language = language

    def __str__(self):
        return f'Song: {self.author} - {self.name}, region: {self.region}/langeage: {self.language}'

    def __repr__(self):
        return f'author={self.author}, name={self.name}, region={self.region}, langeage={self.language}'



classical = ClassicalMusic(author='Ludovico Einaudi', name='Nuvole Bianche', nation="Italian")
popular = PopularMusic(author='A2M', name='I Got Bitches', type='rap')
regional = RegionalMusic(author='BTS', name='FAKE LOVE', region='Asian')
west_classical = WesternClassicalMusic(author='Ludwig Van Beethoven', name='Fur Elise', nation='Germany', era='Early')
rock_music = RockMusic(author='Wheatus', name='Teenage Dirtbag', type='rock', category='pop/alternative/punk-rock')
latin_music = LatinMusic(author='Kaoma', name='Lambada', region='Eastern America', language='Brazilian')

