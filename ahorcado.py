import random


IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = [
    'heladera',
    'auto',
    'casa',
    'skate',
    'bicicleta',
    'motocicleta',
    'computadora',
    'cama',
    'estufa',
    'cortina',
    'mouse',
    'teclado',
    'memoria',
    'cuaderno'    
]


def random_word():
    idx = random.randint(0, len(WORDS) - 1)


def run():
    word = random_word()


if __name__ == '__main__':
    print('B I E N V E N I D O S  A  A H O R C A D O S')
    run()