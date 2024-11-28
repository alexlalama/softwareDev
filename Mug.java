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
    public static void main(String[] args){
        Mug mug1 = new Mug(8, "red", "I miss JuiceWrld");
        System.out.println("Mug1 Attributes:"+ mug1.color+
        " "+ mug1.fillLevel+ " "+mug1.size+" "+ mug1.phrase);
    }    
}

