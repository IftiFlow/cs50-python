def main():
    word = input("Input: ")

    for c in word:
        if c not in ["A","E","I","O","U","a","e","i","o","u"]:
            print(c , end='')
        
main()
