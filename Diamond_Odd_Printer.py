# Delera, Aritz B.

# Make a DiamondPrinter class that we will be using for the program
class DiamondPrinter:
    def __init__(self, n):
        if n % 2 == 0:
            self.is_odd = False
        else:
            self.is_odd = True
            self.n = n

    # define the printing process
    def print_diamond(self):
        if not self.is_odd:
            return "Please provide an odd integer."
            
        # use for loop for upper hand of the diamond
        for i in range(1, self.n, 2):
            spaces = (self.n - i) // 2
            asterisk = i
            print(" " * spaces + "*" * asterisk)

        # use for loop for the middle row of the diamond
        print("*" * self.n)

        # use for loop for the lower half of the diamond
        for i in range(self.n - 2, 0, -2):
            spaces = (self.n - i) // 2
            asterisk = i
            print(" " * spaces + "*" * asterisk)