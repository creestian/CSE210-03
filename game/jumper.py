class Jumper:
    """
    this is the class of the Jumper, where the player seeks to solve a puzzle by guessing the letters of a secret word one at a time
    Attributes:    
        _jumper (list): the parts of the little man.


    """
    
    def __init__(self):
        """ 
        Constructs a new Jumper 
        
        Args:
            self (Jumper): creates a new instance of the class Jumper

        """
        
        
        self._jumper = [    
            '     ___     ',
            '    /___\    ',
            '    \   /    ',
            '     \ /     ',
            '      O      ',
            '     /|\     ',
            '     / \     ',
            '             ',
            '   ^^^^^^^   ' 
        ]  
        self._boolean_value = True  # this is the boolean value that allows says the man to be alive


    def take_life(self):
        """ 
        Deletes the first letter from the list jumper parameter: 
        Args:
            self (Jumper): An instance of Jumper
        """

        self._jumper.pop(0)  # each time the take_life() is called it pops the first element of the list
        if len(self._jumper) == 5:     # conditional if the little man doesn't have any rope
            self._jumper[0] = '     x_x      '   # and add the cross in the head... 
            self._boolean_value = False   #  Remember the boolean value...? here is the response if the list has only four left

    def get_jumper(self):
        """
        Simply returns the list of the jumper to 
        make it print in with the display class methods

        Args:
            self (Jumper): An instance of Jumper

        Returns:
            list: The list of the draw of the little man
        """

        return self._jumper   


    def is_alive(self):
        """
        verify the jumper
        Args:
            self (Jumper): An instance of Jumper

        Returns:
            boolean: the value true if there is a certain amount of items in the list

        """
        # verify the jumper through a simple boolean
        does_live = self._boolean_value
        return does_live      


