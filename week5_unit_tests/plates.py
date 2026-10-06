def main():
    s = input("Enter plate: ")
    if is_valid(s):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <=6):
        return False
    if not s.isalnum():
        return False
    if not s[0:2].isalpha():
        return False
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == "0":
                return False
            if not s[i:].isdigit():
                return False
            break

    return True


if __name__ == "__main__":
    main()