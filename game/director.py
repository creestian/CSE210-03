from game.jumper import Jumper
from game.word import Word
from game.printer import Printer

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _jumper ([Jumper]): One instance of the Jumper class.
        _word ([Word]): One instance of the Word class.
        _printer (boolean): One instance of the Printer class.
    """
    
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._jumper = Jumper()
        self._word = Word()
        self._display = Printer()
        self._user_letter = ''
        self._ran_word = self._word.get_random_word().lower()
        self._guessed_letters = ''
        self._is_alive = True

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self._do_outputs()
        while self._is_alive:
            self._do_inputs()
            self._do_updates()  
            self._do_outputs()

    def _do_updates(self):
        """Ask the user to guess the letter of the word.

        Args:
            self (Director): An instance of Director.
        """
        if self._user_letter.lower() in self._ran_word:
            # User guesses the letter and that is added to the _guessed_letters string
            for i in self._ran_word:
                if i == self._user_letter:
                    self._guessed_letters += self._user_letter
        else:
            # User missed that letter, a life is taken from the jumper
            self._jumper.take_life()

        if sorted(self._ran_word) == sorted(self._guessed_letters):
            # Player guesses the entire word, wons the game
            self._is_alive = False
        if not self._jumper.is_alive():
            # If the jumper is dead the game ends. Player losses
            self._is_alive = False        

    def _do_outputs(self):
        self._display.print_word_so_far(self._ran_word, self._guessed_letters)
        self._display.print_jumper(self._jumper.get_jumper())

    def _do_inputs(self):
        self._user_letter = self._display.get_letter("Guess a letter [a-z]: ")