def square_area(length):
    '''
    
    '''
    if length < 0:
        return None
    value = length*length
    return value

def test_square_area_6():
     value = square_area(6)
     assert value == 36

def test_square_area_8():
    value = square_area(8)
    assert value == 64

def test_length_less_than_zero():

    value = square_area(-2) 
    assert None == value