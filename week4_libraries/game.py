import random

def main():
    while True:
        try:
            user_input = int(input("Level: "))

            if user_input <= 0:
                continue
            else:
                
                level = random.randint(1 , user_input)
                break
            

        except ValueError:
            continue

        

    while True:
        try:
            guess = int(input("Guess: "))

        except ValueError:
            continue

        if guess <= 0:
            continue

        elif guess < level:
            print("Too small!")

        elif guess > level:
            print("Too large!")

        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()

        
