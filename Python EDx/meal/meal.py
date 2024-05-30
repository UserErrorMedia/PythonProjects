#This script triggers an alert for the type of meal depending on the time of day

def main():

    answer = input("What time is it? ")
    time = convert(answer)

# Breakfast between 7 - 8 am
    if 7 <= time <= 8:
        print("breakfast time")
# Lunch between 12 - 1 pm
    elif 12 <= time <= 13:
        print("lunch time")
# Dinner between 6 - 7 pm
    elif 18 <= time <= 19:
        print("dinner time")
    else:
        print("")

def convert(time):
    hours, minutes = time.split(":")
    minute = float(minutes) / 60
    return float(hours) + minute

if __name__ == "__main__":
    main()