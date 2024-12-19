"""
types of variables
alexandra n. lalama
"""
def variable_practice():
    age_in_months = 267
    number_of_days_in_a_year = 365
    name_of_first_pet = "Munchie"
    five_dig_of_pi = 3.14159
    print("Age in months:", age_in_months)
    print("Number of days in a year:", number_of_days_in_a_year)
    print("Name of first pet:", name_of_first_pet)
    print("First five digits of pi:",five_dig_of_pi)
def expressions_practice():
    """
    practicing arithmitic 
    """
    literal = 'Literal String'
    addition_eq = 4 +4
    exponent_eq = 3*2
    floor_division_eq = 12/4
    mod_eq = 18/4 
    pemdas = (4 + 2)*(3-2) # 6 
    print(literal)
    print(addition_eq)
    print(exponent_eq)
    print(floor_division_eq)
    print(mod_eq)
    print(pemdas)

def prompt_and_print():
    """
    Prompts a user for (2) numeric values 
    Prints the result of addition, subtraction, 
    multiplication, and division of the two numbers
    """
    num1= float(input("Enter a numeric value: "))
    num2= float(input("Enter a numeric value: "))
    addition = num1 + num2
    subtracting = num1-num2
    multiplying = num1 * num2
    division = num1 / num2
    print(num1, "+",num2, "=", addition)
    print(num1, " - ",num2, "=",subtracting)
    print(num1, "*",num2, "=",multiplying)
    print(num1, "/",num2, "=", division)

def main():
    # variable_practice()
    # expressions_practice()
    prompt_and_print()
main()