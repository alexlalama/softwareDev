def check_guess(answer, guess):
    '''
    Checks player's guess 
    '''
    
    return -1

def test_check_guess_range_low():
    guess = check_guess(2, -1)
    assert guess == -1