def main():
    grocery_list = {}
    while True:
        
        try:
            user_input = input().upper()
        except EOFError:
            break

        try:
            grocery_list[user_input] += 1
        except KeyError:
            grocery_list[user_input] = 1
            
        

    for item in sorted(grocery_list):
        print(f"{grocery_list[item]} {item}")
        
main()

