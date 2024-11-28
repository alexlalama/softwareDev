class Mug:
    '''Class to represent a Mug'''
    # attributes, each attribute ro variable is a field
    __slots__ = ['__size', '__color', '__fill_level', '__phrase']
    
    
    #creating a default constructor to 'guarantee that every object has a value for every attribute'
    def __init__(self, size, color, phrase):
        self.__size = size
        self.__color = color
        self.__fill_level = 0
        self.__phrase = phrase
    
    '''
    fill method adds an amount of ounces to the fill level
        if filled over the size level returns the size
    returns the fill level
    '''
    def fill(self,ounces):
        self.__fill_level += ounces
        if ounces > self.__size:
            self.__fill_level= self.__size
        return self.__fill_level
    
    '''
    drain method removes amount of ounces to the fill level
        if fill level goes below zero mug fill level is 0
    returns the fill level
    '''
    def drain(self,ounces):
        self.__fill_level -= ounces
        if self.__fill_level < 0:
            self.__fill_level = 0
        drained = self.__fill_level- ounces
        return drained

'''
main function
'''
def main():
    mug1 = Mug(8, "red", "I miss JuiceWrld")
    mug2 = Mug(12, "gray", "I miss school")
    #Mug1: 8 red I miss JuiceWrld
    print("Mug1: ",mug1.size,mug1.color, mug1.fill_level ,mug1.phrase)
    #Mug2: 12 gray I miss school
    print("Mug2",mug2.__size,mug2.__color, mug2.__fill_level ,mug2.__phrase)
    mug1.fill(12)
    print(mug1.__fill_level)
    mug1.drain(3)
    print(mug1.__fill_level)
    mug2.fill(7)
    print(mug2.__fill_level)
    mug2.drain(2)
    print(mug2.__fill_level)
if __name__ == "__main__":
    main()