def main():
    user_input = input("Type the expression: ")
    result = calculate(user_input)
    print(f"{result:.1f}")

def calculate(expression):
    x,y,z = expression.split(" ")

    x = float(x)
    z = float(z)

    if y == '+':
        return x + z
    elif y == '-':
        return x - z
    elif y == '*':
        return x * z
    elif y == '/':
        return x / z

main()






