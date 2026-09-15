def main():
    camel_case = input("Camel Case: ")
    print("Snake Case: " , end='')
    snake_case(camel_case)

def snake_case(s):
    for c in s:
        if c.isupper() == True:
            print("_" + c.lower() , end='')

        else:
            print(c , end='')

main()



