def square_area(length):
    '''
    
    '''
    value = length*length
    return value

def test_square_area_6():
    value = square_area(6)
    assert value == 36

def test_square_area_8():
    value = square_area(8)
    assert value == 64
