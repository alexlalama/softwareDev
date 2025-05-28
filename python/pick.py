import random

def is_correct(guess, answer):
    return guess == answer


def check_guess(guess, answer):
    if(answer == guess):
        return 0
    

def test_check_guess_correct():
    #assert
    answer = 0
    guess = 0
    #invoke
    
    #analyze
    assert check_guess(guess, answer) == 0 

def main():
    '''answer = random.randint(1, 10)
    guess = int(input("Enter a random number 1 - 10"))
    print(is_correct(guess, answer))'''
main()