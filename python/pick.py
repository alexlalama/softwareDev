import random

def is_correct(guess, answer):
    return guess == answer


def check_guess(guess, answer):
    if(answer == guess):
        return True
    elif(answer !=guess):
        return False
    else:
        return 0
def main():
    answer = random.randint(1, 10)
    guess = int(input("Enter a random number 1 - 10"))
    print(is_correct(guess, answer))
if __name__ == "main()":
    main()