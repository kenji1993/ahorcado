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
    return WORDS[idx]


def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('--- * --- * --- * --- * --- *')


def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        current_letter = str(input('Elige una letra: '))

        letter_indexes = []
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)


        if len(letter_indexes) == 0:
            intentos += 1
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter

            letter_indexes




if __name__ == '__main__':
    print('B I E N V E N I D O S  A  A H O R C A D O S')
    run()