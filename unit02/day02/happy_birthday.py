"""
Asks users for their name, birth month, birth day
birth year and prints to standard output
"""
def bday_message():
    name = input("Enter your name: ")
    birth_month = input("Enter your birth month: ")
    birth_day = input("Enter your birth day of the month: ")
    birth_year = input("Enter your birth year: ")
    print(name, " your birthday is on ", birth_month, " ",birth_day, ",", birth_year,"!", sep="")

def main():
    bday_message()
    bday_message()
    bday_message()

main()