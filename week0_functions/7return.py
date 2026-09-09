def main():
    x = int(input("Enter the number to square : " ))
    print("Square of the no. is" , square(x))

def square(n):
    return n * n 
    # or you can use n**2 which means 2 is raised to the power n
    # or you can use pow(n , 2)

main()
