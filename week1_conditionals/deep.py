def main():
    ans = input("What is the Answer?").lower().strip()

    match ans:
        case "42" | "forty two" | "forty-two":
            print("Yes")
        case _:
            print("No")

main()