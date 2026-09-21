def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            n = int(input("What's x? "))
            return n
        except ValueError:
            pass

main()