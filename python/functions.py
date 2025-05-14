"""
    Program to calculate Birthday in Months and day of year
    Alex Lalama
"""
def birthday_in_months():
    """
    Calulates birthday in months
    """
    current_year  =int(input("Enter the current year: ")) # current year
    current_month = int(input("Enter the current month: ")) # current month
    year = int(input("Enter your birth year: "))  # birthday year
    month = int(input("Enter your birth month: ")) # birthday month

    age_in_months = (((current_year - year) *12) - (current_month-month))

    print("Your age in months: ", age_in_months)

def current_day_of_month():
    """
    Calulates day of the year
    """
    month = int(input("Enter the month: "))
    day_of_month = int(input("Enter the day of the month: "))
    day_of_year = (month*30.4)+day_of_month # month times 30.4 plus day of the month
    print("The approximate day of the year is: ",day_of_year) #prints result

def main():
    birthday_in_months()
    current_day_of_month()
main()