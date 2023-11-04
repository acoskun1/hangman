import random
from typing import List





if __name__ == "__main__":

    word_list: List[str] = list(['apple', 'banana', 'watermelon', 'pineapple', 'strawberry'])
    
    word: str = random.choice(word_list)

    print(word_list)
    print(word)

    guess: str = input('Enter a single letter: ').lower()
    if guess.isalpha() and len(guess) == 1:
        print('Good guess')
    else:
        print('Oops! That is not a valid input.')

