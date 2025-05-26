import random
def test_check_guess_range_low():
    answer = 2
    guess = 9
    assert check_guess(guess, answer) == 'Too high'


def test_check_guess_range_high():
    guess = 9
    answer = 2
    assert check_guess(guess, answer) == 'Too low!'


def test_check_guess_range_correct():
    answer = 2
    guess = 2
    assert check_guess(guess, answer) == 'Correct'


def test_check_guess_out_range_():
    answer = 11
    guess = 2
    assert check_guess(guess, answer) == 'Guess out of range'


def check_guess(guess, answer):
    while(guess != answer):
        if(guess > 10):
            return "Guess out of range"
        elif (guess < answer):
            return 'Too low!'
        else: 
            return 'Too high'
    return "Correct"


def main():
    answer = random.randint(1,10)
    i = 0
    while(i<3):
        i +=1
        guess = int(input("Enter a number between 1 - 10: "))
        print(check_guess(guess, answer))
        if(i == 3):
            g = 'Game over'
            print(g)
            return
main()
