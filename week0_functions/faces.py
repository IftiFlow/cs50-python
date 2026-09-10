def main():
    user_input = input("Type here: ")
    print(convert(user_input))

def convert(text):
    return text.replace(":)","🙂").replace(":(","🙁")

main()


