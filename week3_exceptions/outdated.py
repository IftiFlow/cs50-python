months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    while True:
        try:
            user_input = input("Date: ").strip()

            if '/' in user_input:
                month , day , year = user_input.split("/")
                month = int(month)
                day = int(day)
                year = int(year)

            elif ',' in user_input:
                month , day , year = user_input.split(" ")
                month = months.index(month.title()) + 1
                day = day.replace("," , "")
                
                day = int(day)
                year = int(year)

            else:
                continue

        except (ValueError , KeyError):
            continue

        if day > 31 or month > 12:
            continue

        print(f"{year}-{month:02}-{day:02}")
        break

main()



