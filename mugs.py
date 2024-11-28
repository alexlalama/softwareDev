class Mug:
    '''Class to represent a Mug'''
    # attributes, each attribute ro variable is a field
    __slots__ = ['size', 'color', 'fill_level', 'phrase']
    #creating a default constructor to 'guarantee that every object has a value for every attribute'

    def __init__(self, size, color, phrase):
        self.size = size
        self.color = color
        self.fill_level = 0
        self.phrase = phrase


def main():
    mug1 = Mug(8, "red", "I miss JuiceWrld")
    mug2 = Mug(12, "gray", "I miss school")
    #Mug1: 8 red I miss JuiceWrld
    print("Mug1: ",mug1.size,mug1.color, mug1.fill_level ,mug1.phrase)
    #Mug2: 12 gray I miss school
    print("Mug2",mug2.size,mug2.color, mug2.fill_level ,mug2.phrase)
       
if __name__ == "__main__":
    main()