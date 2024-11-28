public class Mug {
    // Attributes
    int size;
    String color;
    int fillLevel;
    String phrase;

    public Mug(int size, String color, String phrase){
        this.size = size;
        this.color = color;
        this.phrase = phrase;
    }
    /*
     * fill method adds an amount of ounces to the fill level
     * if filled over the size level returns the size
     * returns the fill level
     */
    
    public int fill(int ounces){
        this.fillLevel += ounces;
        if(ounces > this.size){
            this.fillLevel = this.size;
        }
        return this.fillLevel;
    }
    /*
     * drain method removes amount of ounces to the fill level
     * if fill level goes below zero mug fill level is 0
     * returns the fill level
     */
    public int drain(int ounces){
        this.fillLevel -= ounces;
        if(this.fillLevel < 0){
            this.fillLevel = 0;
        }
        int drained = this.fillLevel -ounces;
        return drained;
    }
    public static void main(String[] args){
        Mug mug1 = new Mug(8, "red", "I miss JuiceWrld");
        System.out.println("Mug1 Attributes:"+ mug1.color+
        " "+ mug1.fillLevel+ " "+mug1.size+" "+ mug1.phrase);
        mug1.fill(12);
        System.out.println(mug1.fillLevel);
        mug1.drain(3);
        System.out.println(mug1.fillLevel);
        
    }    
}

