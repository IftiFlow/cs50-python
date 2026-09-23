import sys
from random import choice
from pyfiglet import Figlet

def main():
    figlet = Figlet()

    if len(sys.argv) == 3:

        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            sys.exit(1)

        if sys.argv[2] not in figlet.getFonts():
            sys.exit(1)

        figlet.setFont(font=sys.argv[2])

    elif len(sys.argv) == 1:
        random_font = choice(figlet.getFonts())
        figlet.setFont(font=random_font)

    else:
        sys.exit(1)

    user_input = input("Input: ")
    print(figlet.renderText(user_input))

if __name__ == "__main__":
    main()





