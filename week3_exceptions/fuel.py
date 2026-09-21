def main():
    fraction = Get_Fraction()
    Output(fraction)

def Get_Fraction():
    while True:
        try:
            user_input = input("Fraction: ")
            x , y = user_input.split("/")
            x = int(x)
            y = int(y)

            if (x > y) or (x * y < 0):
                continue
            

            f = round( (x/y) * 100 )

        except (ValueError , ZeroDivisionError):
            pass
        else:
            return f

def Output(n):
    if n <= 1.0:
        print("E")
    elif n >= 99.0:
        print("F")
    else:
        print(f"{n}%")

main()


        


