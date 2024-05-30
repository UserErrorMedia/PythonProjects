list = [
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

while True:
    # Prompt user for date
    date = input("Date: ")
    try:
        month, day, year = date.split("/")
        if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
            break
    except:
        try:
            new_month, new_day, year = date.split(" ")
            for i in range(len(list)):
                if new_month == list[i]:
                    month = i + 1
            day = new_day.replace("," , "")
            if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
                break
        except:
            print()
            pass

print(f"{int(year)}-{int(month):02}-{int(day):02}")