def age_in_months():	
    year = int(input("Current Year: "))
    month = int(input("Current month: "))
    birth_year = int(input("Birth year: "))
    birth_month = int(input("Birth month: "))
    age_in_months = int(((year -birth_year)*12)+(month - birth_month))
    print(age_in_months)

def day_of_year():
    month = float(input("Enter the month: "))
    day_of_month = float(input("Enter the day of month: "))
    day_of_year = float((month * 30.4)-(30.4 -day_of_month))
    print("The approximate day of the year is: ", day_of_year)
def main():
    age_in_months()
    age_in_months()
    age_in_months()
    day_of_year()
    day_of_year()
    day_of_year()
main()
