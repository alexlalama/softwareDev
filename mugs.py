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
    
    '''
    fill method adds an amount of ounces to the fill level
        if filled over the size level returns the size
    returns the fill level
    '''
    def fill(self,ounces):
        self.fill_level += ounces
        if ounces > self.size:
            self.fill_level= self.size
        return self.fill_level
    
    '''
    drain method removes amount of ounces to the fill level
        if fill level goes below zero mug fill level is 0
    returns the fill level
    '''
    def drain(self,ounces):
        self.fill_level -= ounces
        if self.fill_level < 0:
            self.fill_level = 0
        drained = self.fill_level- ounces
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
    print("Mug2",mug2.size,mug2.color, mug2.fill_level ,mug2.phrase)
    mug1.fill(12)
    print(mug1.fill_level)
    mug1.drain(3)
    print(mug1.fill_level)
    mug2.fill(7)
    print(mug2.fill_level)
    mug2.drain(2)
    print(mug2.fill_level)
if __name__ == "__main__":
    main()