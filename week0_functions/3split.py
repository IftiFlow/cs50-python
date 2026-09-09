name = input("What's your name? ").strip().title()

#We want to split the words on " " now

first,middle,last = name.split(" ")

print(f"Hey, {first} , {last} , {middle}")

