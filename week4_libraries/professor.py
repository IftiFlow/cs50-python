import random


def main():
    score = 0
    level = get_level()
    for _ in range(10):
        
        X = generate_integer(level)
        Y = generate_integer(level)

        wrong = 0

        for _ in range(3):
            
            try:
                ans = int(input(f"{X} + {Y} = "))

                if ans == X + Y:
                    score += 1
                    break

                else:
                    print("EEE")
                    wrong += 1

            except ValueError:
                wrong += 1
                print("EEE")
                

        if wrong == 3:
            print(f"{X} + {Y} = {X+Y}")

    print("Score: " , score)


def get_level():
    while True:
        try:
            user_input = int(input("Level: "))
        except ValueError:
            continue

        if user_input not in [1 , 2 , 3]:
            continue

        else:
            return user_input


def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)
    else:
        raise ValueError
        
    


if __name__ == "__main__":
    main()