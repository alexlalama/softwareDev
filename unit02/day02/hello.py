"""
Hello World function and Customized Hello You function

Alexandra N. Lalama
"""

def hello_world():
    """
    prints Hello, Again, World!!!
    """
    print("Hello, Again, World!!!") #using the print() function to return a literal string

def hello_you():
    """
    Prompts the user for their name and prints 
    a customized hello message with their name
    """
    name = input("Enter your name: ") #prompts the user for their name
    print("Hello, ", name, "!", sep="") #prints Hello, name!


def main():
    hello_world() #call to a function
    hello_you()

main()