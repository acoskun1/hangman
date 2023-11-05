#!/usr/bin/python3

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
            print(self.word_guessed)
        
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} left')

        self.list_of_guesses.append(guess)


    def ask_for_input(self) -> None:
        guess: str = input('Guess a letter: ')
        if not guess.isalpha() or len(guess) != 1:
            print('Invalid letter. Please, enter a single alphabetical character.')
        elif guess in self.list_of_guesses:
            print('You have already tried that letter!')
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)

def play_game(word_list: List[str]):

    game = Hangman(word_list, num_lives=5)

    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters == 0:
            print("Congratulations. You wont the game!")
            break
        else:
            game.ask_for_input()

if __name__ == '__main__':
    word_list: List[str] = ['apple', 'banana', 'orange', 'strawberry', 'watermelon']
    play_game(word_list)

