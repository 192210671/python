def get_season(month, day):
    if (month == "Mar" and day >= 20) or (month == "Apr") or (month == "May") or (month == "Jun" and day < 21):
        return "Spring"
    elif (month == "Jun" and day >= 21) or (month == "Jul") or (month == "Aug") or (month == "Sep" and day < 22):
        return "Summer"
    elif (month == "Sep" and day >= 22) or (month == "Oct") or (month == "Nov") or (month == "Dec" and day < 21):
        return "Fall"
    else:
        return "Winter"

month_input = input("Enter the month (e.g., Jan, Feb, Mar): ")
day_input = int(input("Enter the day of the month: "))


result_season = get_season(month_input, day_input)
print(f"The season is {result_season}.")

