def check_guess(answer, guess):
    '''
    Checks player's guess 
    '''
    if guess < answer or guess > answer:
        return "Guess out of range"
    
def test_check_guess_range_low():
    guess = check_guess(2, -1)
    assert guess == "Guess out of range"

def test_check_guess_range_high():
    guess = check_guess(6, 11)
    assert guess == "Guess out of range"