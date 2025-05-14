def variable_practice():
    age_in_months = 12 * 22
    number_of_days = 365
    first_pet = "Munchie"
    pi = 3.14159
    print(age_in_months)
    print(number_of_days)
    print(first_pet)
    print(pi)

def expressions_practice():
    a_sentence= "A string literal"
    adding = 3 +5  #8
    an_exponent = 4**2 #16
    divison = 12/4 # 3
    mod = 12/5 # 2.4
    add_sub = (3+7)*(3-2) # 10*1 = 1
    mix_operators = ((3 + 5) /2) **2 #16
    print(a_sentence)
    print(an_exponent)
    print(divison)
    print(mod)
    print(add_sub)
    print(mix_operators)

def prompt_and_print():
    num1 = int(input("Enter a number: "))
    num2 = int( input("Enter a number: "))
    add = num1 + num2
    multi = num1 * num2
    sub = num1 -num2
    divide = num1 / num2
    print(num1, " + ", num2 , " = ",add)
    print(num1, " * ", num2 ," = ",multi)
    print(num1, " - ", num2 ," = ",sub)
    print(num1, " / ", num2 ," = ",divide)    
                 
def main():
    variable_practice()
    expressions_practice()
    prompt_and_print()
main()