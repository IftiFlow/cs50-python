def main():
    size = int(input("Enter length: "))
    print_square(size)

def print_square(n):
    for i in range(n):
        # for j in range(n):
        #     print("#" , end='')
        # print()

        print("#" * n)

main()