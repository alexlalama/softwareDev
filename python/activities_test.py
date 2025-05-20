def square_area(length):
    area = length * length
    return area 

def test_square_area_8():
    """
    find area of a square with side of eight
    """
    x = square_area(8)
    assert x == 64

def test_square_area_6():
    """
    find area of a square with side of eight
    """
    x = square_area(6)
    assert x == 36

def test_square_area_negative():
    # find area of negative square length
    x= square_area(-6)
    assert None
