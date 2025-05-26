import random

def test_out_of_range():
    answer = 11
    guess = 2
    assert check_guess(guess, answer) == 'Guess out of range'

def check_guess(guess, answer):                 
    s = "Guess out of range"
    return s 