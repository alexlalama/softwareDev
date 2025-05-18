def convert_height():
    '''
    convert height from inch to feet and inches
    '''
    height = int(input("Enter your height in inches: "))
    feet = (height//12)
    inches = height%12
    print("You are ", feet ,"' ", inches," tall")

def main():
    convert_height()

main()