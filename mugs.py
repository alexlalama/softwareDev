class Mug:
    '''Class to represent a Mug'''
    # attributes, each attribute ro variable is a field
    __slots__ = ['size', 'color', 'fill_level', 'phrase']


def main():
    mug1 = Mug()
    mug1.color = "gray"
    mug1.size = "12"
    mug2 = Mug()
    mug2.phrase = "I miss JuiceWrld"
    mug2.color = "brown"
    # attribute error because mug1 does not have an phrase attribute assigned to its instance of a class
    # print(mug1.phrase)
    # Mug1 Color: gray Mug1 Size: 12
    print("Mug1 Color:",mug1.color,"Mug1 Size:", mug1.size)
    #Mug1 Color: brown Mug1 Phrase: I miss JuiceWrld
    print("Mug1 Color:",mug2.color,"Mug1 Phrase:",mug2.phrase)
       
if __name__ == "__main__":
    main()