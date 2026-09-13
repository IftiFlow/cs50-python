def main():
    height = int(input("No. of blocks in column: "))
    print_column(height)

def print_column(n):
    # for _ in range(n):
    #     print("#")

    print( "#\n" * n , end='')

main()
