def check_guess(answer, guess):
    '''
    Checks player's guess 
    '''
    if guess < 1 or guess > 10:
        return "Guess out of range"
    if guess < answer:
        return "Too low!"
    if guess > answer:
        return "Too high!"
    return ''
def test_check_guess_range_low():
    guess = check_guess(2, -1)
    assert guess == "Guess out of range"

def test_check_guess_range_high():
    guess = check_guess(6, 11)
    assert guess == "Guess out of range"

def test_check_guess_too_low():
    guess = check_guess(2,1)
    assert guess == "Too low!"

def test_check_guess_too_high():
    guess = check_guess(4,9)
    assert guess == "Too high!"

def test_check_guess_correct():
    guess = check_guess(3,3)
    assert guess == "Correct"
