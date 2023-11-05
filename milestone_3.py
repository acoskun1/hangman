import random
from typing import List

def check_guess(guess: str) -> None:
    guess = guess.lower()
    if guess in word:
        print(f'Good guess! {guess} is in the word')
    else:
        print(f'Sorry, {guess} is not in the word. Try again')

def ask_for_input() -> None:
    while True:
        guess: str = input('Guess a letter: ').lower()
        if guess.isalpha() and len(guess) == 1:
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character')

    check_guess(guess)

if __name__ == "__main__":
    
    fruits: List[str] = list(['apple', 'banana', 'orange', 'strawberry', 'grape'])
    word: str = random.choice(fruits)
    #guess: str = ask_for_input()
    #check_guess(guess)
    print(word)
    ask_for_input()
