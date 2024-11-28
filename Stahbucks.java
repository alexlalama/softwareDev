public class Stahbucks{
    public static void main(String[] args){
        Mug mug1 = new Mug(-10, "red", "I miss JuiceWrld");
        System.out.println("Mug1 Attributes:"+ mug1.color+
        " "+ mug1.fillLevel+ " "+mug1.size+" "+ mug1.phrase);
        mug1.fill(12);
        System.out.println(mug1.fillLevel);
        mug1.drain(3);
        System.out.println(mug1.fillLevel);
        
        // Practing encapulsation to see if attribute can be accessed from another class
        System.out.println(mug1.getSize());
        
    }   
}