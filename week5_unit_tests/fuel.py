def main():
    fraction = input("Enter fraction: ")
    percentage = (convert(fraction))
    fuel_status = gauge(percentage)
    print(fuel_status)


def convert(fraction):
    x , y = fraction.split('/')

    x = int(x)
    y = int(y)

    if y == 0:
        raise ZeroDivisionError
    
    if (x > y) or (x * y < 0):
        raise ValueError
    

    return round((x/y)*100)

     
def gauge(percentage):
    if percentage <= 1.0:
        return "E"
    elif percentage >= 99.0:
        return "F"
    else:
        return f"{percentage}%"
    


if __name__ == "__main__":
    main()