def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            n = int(input(prompt))
            return n
        except ValueError:
            pass

main()