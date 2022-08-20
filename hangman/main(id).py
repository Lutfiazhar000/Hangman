import random
from indonesianWords import words
from hangman_visual import lives_visual_dict
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('Kamu memiliki', lives, 'nyawa tersisa dan kamu sudah menggunakan huruf-huruf ini: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Kata saat ini: ', ' '.join(word_list))

        user_letter = input('Tebak huruf: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nHuruf kamu,', user_letter, 'tidak termasuk dalam kata.')

        elif user_letter in used_letters:
            print('\nKamu sudah menggunakan huruf ini. Tebak huruf yang lain.')

        else:
            print('\nHuruf yang kamu masukkan kurang tepat.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('Kamu kalah, maaf. Kata yang di maksud adalah', word)
    else:
        print('YAY! Kata yang kamu terbak benar', word, '!!')


if __name__ == '__main__':
    hangman()
