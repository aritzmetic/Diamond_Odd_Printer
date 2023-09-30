# Delera, Aritz B.

# import DiamondPrinter class
from Diamond_Odd_Printer import DiamondPrinter

import pyfiglet
import time

opening = pyfiglet.figlet_format("= D.S.A =", font = "starwars")
print(opening)


# Create an introduction
print("=" * 51)
print("\033[32m Welcome to AritzMetic's Odd Diamond Printer! \033[0m".center(60, "+"))
print("=" * 51)

# Ask the name of the user to create a greeting
name = input("\033[34mHi Smart Pipol! what is your name?\033[0m")

time.sleep(1)
print()

print(f"\033[34mHello, {name}! Let's play a quick game.\033[0m")

time.sleep(1)

answer = input("\033[34mDo you like diamonds? (yes/no): \033[0m").lower()

time.sleep(1)
print()

if answer == "yes":
    print("\033[45mAYOOOO! Diamonds are Fantastic!\033[0m")
elif answer == "no":
    print("\033[45mOKIIIII! Well, Diamonds might not be for everyone.\033[0m")
else:
    print("\033[45mBalakadiyan, but let's continue.\033[0m")

time.sleep(1)
print("=" * 51)
print("\033[32m Loading... \033[0m".center(60))
print("=" * 51)
time.sleep(1)

# define and get the user input
def user_input():
    # use try and except method
    while True:
        try:
            n = int(input("\033[35mPlease enter your ODD Integer: \033[0m"))
            if n % 2 == 1:
                time.sleep(1)
                print("=" * 51)
                print("\033[33m Processing Your Diamond...\033[0m".center(60))
                print("=" * 51)
                time.sleep(1)
                print()
                return n

            else:
                print("\033[31mPlease provide an odd integer.\033[0m")
        except ValueError:
            print("\033[31mInvalid input. Please enter an integer.\033[0m")

# call the method/s
if __name__ == "__main__":
    n = user_input()
    diamond_printer = DiamondPrinter(n)
    diamond_printer.print_diamond()

    closing = pyfiglet.figlet_format("Thank you for using AritzMetic's Diamond Printer. Have a nice day!", font="bubble")
    print(closing)