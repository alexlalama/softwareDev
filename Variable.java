/**
 * A class to define variable types
 * @author Alexandra N. Lalama
 * @version 20241122
 */
 public class Variable
 {
   public static void main(String[] args)
   {  
         // variable names may contain [A-Z], [a-z], [0-9] or _
         // Declaring variables: integers, double(fractional), and object variables
         // reference to a location in memory holding that variable name 
         int testInt;
         double testDouble;
         String testString;
         // Initializing variables
         // equals means the assigns the value of 
         testInt = 2;
         testDouble = 47.3; 
         testString = "A string";
         // both
         int testInt2 = 10;
         System.out.println(testInt2);
         // 2 + 10 = 12
         int testInt3 = testInt + testInt2;
         System.out.print(testInt3);
   }
 }