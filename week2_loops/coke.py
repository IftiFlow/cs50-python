def main():
    Amount_due = 50

    while Amount_due > 0:
        print(f"Amount Due: {Amount_due}")
        coin = int(input("Insert coin: "))

        if coin in [25,10,5]:
            Amount_due -= coin 

    change = abs(Amount_due)
    print(f"Change Owed: {change}")

main()
    







