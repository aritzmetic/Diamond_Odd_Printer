# Delera, Aritz B.

# import DiamondPrinter class
from Diamond_Odd_Printer import DiamondPrinter

# define and get the user input
def user_input():
    # use try and except method
    while True:
        try:
            n = int(input("Please enter an ODD Integer: "))
            if n % 2 == 1:
                return n
            else:
                print("Please provide an odd integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

# call the method/s
if __name__ == "__main__":
    n = user_input()
    diamond_printer = DiamondPrinter(n)
    diamond_printer.print_diamond()