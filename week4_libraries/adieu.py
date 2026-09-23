from inflect import engine
p = engine()

def main():
    names = []
    while True:
        try:
            user_input = input("Name: ")
            names.append(user_input)
            
        except EOFError:
            print()
            break 

        

    print("Adieu, adieu, to " + p.join(names) )  

if __name__ == "__main__":
    main()
 
