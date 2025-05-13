"""
    Prints hello messages
    Alex Lalama
"""
def hello():
    """
    Prints Hello, world
    """
    print("Hello, world !") #prints message
def hello_you():
    """
    Prompts a user for their name and prints a hello message
    """
    name = input("Enter name: ") # prompts user for name
    print("Hello, ", name) #prints 'Hello, ' with the name

def main():
    
    hello_you()

main()