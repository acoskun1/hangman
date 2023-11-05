import random
from typing import List

class Hangman:

    def __init__(self, word_list: List[str], num_lives: int =5) -> None:
        self.word: str = random.choice(word_list)
        self.word_guessed: List[str] = list('_' * len(self.word))
        self.num_letters: int= len(set(list(self.word)))
        self.num_lives: int = num_lives
        self.list_of_guesses: List[str] = list()

    def check_guess(self, guess: str) -> None:
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            letter_index: int = 0
            for position, letter in enumerate(self.word):
                if letter == guess:
                    letter_index = position
                    self.word_guessed[letter_index] = letter
            
            self.num_letters -= 1


    def ask_for_input(self) -> None:
        while True:
            guess: str = input('Guess a letter: ')
            if not guess.isalpha() and len(guess) != 1:
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You have already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'strawberry', 'watermelon', 'grapes', 'blueberry', 'raspberry']
    hangman = Hangman(word_list, num_lives=5)
    print(hangman.word)
    hangman.ask_for_input()


