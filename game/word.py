from random import *
#the class Word is to choose the words
class Word:
    
    #This function is to list the words of the game.
    def __init__(self):
        self._word = ["alpha", "shift", "words", "delta", "name", "stars"] 

    #This function will return a random word from the list
    def get_random_word(self):
    
        index = randint(0, len(self._word) - 1)
        return self._word[index]