def main():    
    user_input = int(input("Enter the number: "))
    
    if is_even(user_input):
        print("Even")

    else:
        print("Odd")

def is_even(n):
    return n % 2 == 0

main()
    


