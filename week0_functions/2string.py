#Ask the user their name
name = input("What's your name? ")

#Remove whitespaces from the name using strip
name = name.strip()

#Capitalize the first letter
name = name.capitalize()

print(f"Hey , {name}")

#Using \n here to print the name in a newline
name = input("What's your name?\n").strip().title()
print(f"Hey , {name}")