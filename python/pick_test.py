import pick
def test_check_guess_correct():
    #assert
    answer = 0
    guess = 0
    #invoke
    
    #analyze
    assert pick.check_guess(guess, answer) == True 
def test_check_guess_incorrect():
    answer =2 
    guess = 3
    assert pick.check_guess(guess, answer) == False
