import random
def test_check_guess_range_low():
    assert check_guess(9, 2) == 'Too high'


def test_check_guess_range_high():
    assert check_guess(2, 9) == 'Too low!'


def test_check_guess_range_correct():
    assert check_guess(2, 2) == 'Correct'


def test_check_guess_range_():
    assert check_guess(11, 2) == 'Guess out of range'


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
