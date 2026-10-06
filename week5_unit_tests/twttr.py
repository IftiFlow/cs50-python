def main():
    word = input("Enter the word: ")
    word = shorten(word)
    print(word)


def shorten(word):
    result = ""
    for c in word:
        if c not in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' , '1'}:
            result += c

    return result
            


if __name__ == "__main__":
    main()