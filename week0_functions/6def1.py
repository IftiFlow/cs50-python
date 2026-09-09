def main():
    name = input("What's your name? ").title()
    hello(name)

def hello(to="bro"):
    print("Hello," , to)

main()