class Printer:
    
    '''
    The printer prints the output for the jumper
    '''
    
    #Prints the jumper according to the quantity of attempts remaining.
    def print_jumper(self, jumper): 
        print()
        print()
        for line in jumper:
            print(line)

    #Print the message to get the letter
    def get_letter(self, message): 
        letter = input(message)
        return letter
    #A loop to print the chosen word, if not it will print "_"
    def print_word_so_far(self, word, guessed_letter): 

        for letter in word:
            if letter in guessed_letter:
                print(letter, end="") 
            else:
                print("_", end="")
        

