public class Mug {
    // Attributes
    private int size;
    private String color;
    private int fillLevel;
    private String phrase;

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
    /*
     * accesors
     */
    public int getSize(){
        return this.size;
    }
    public int getFillLevel(){
        return this.fillLevel;
    }
    public String getPhrase(){
        return this.phrase;
    }
    public String getColor(){
        return this.color;
    }
    /*
     * Mutators
     */
    public void setPhrase(String phrase){
        this.phrase = phrase;
    }
    public static void main(String[] args){
        Mug mug1 = new Mug(8, "red", "I miss JuiceWrld");
        System.out.println("Mug1 Attributes:"+ mug1.color+
        " "+ mug1.getFillLevel()+ " "+mug1.getSize()+" "+ mug1.getPhrase());
        mug1.fill(12);
        System.out.println(mug1.fillLevel);
        mug1.drain(3);
        System.out.println(mug1.fillLevel);
        
    }    
}

