def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("Enter n: "))
        if n > 0:
            return n 

def meow(num):
    for _ in range(num):
        print("meow")

main()