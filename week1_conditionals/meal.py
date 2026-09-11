def main():
    user_input = input("What time is it? ")
    time_float = convert(user_input)

    if 7.0 <= time_float <= 8.0:
        print("breakfast time")
    elif 12.0 <= time_float <= 13.0:
        print("lunch time")
    elif 18.0 <= time_float <= 19.0:
        print("dinner time")


def convert(time):
    hrs , mins = time.split(":")
    return float(hrs) + (float(mins) / 60)

if __name__ == "__main__":
    main()