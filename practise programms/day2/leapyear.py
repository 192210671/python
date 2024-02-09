def is_leap_year(year):
    if (year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0)):
        return True
    else:
        return False


try:
    year = int(input("Enter a year: "))
    
    if year > 0:
        if is_leap_year(year):
            print(f"{year} is a Leap Year.")
        else:
            print(f"{year} is a Non-Leap Year.")
    else:
        print("Please enter a valid positive year.")
except ValueError:
    print("Please enter a valid integer for the year.")

