public class TestStudent
{
   public static void main(String[] args)
   {
      Student stu1 = new Student("Person" , "Last", 34332, 3.2);
      Student stu2 = new Student("Don" , "Ws", 35675, 1.2);      

      System.out.println(stu1.toString());
      stu1.setNewStudentId();
      System.out.println(stu1.toString());
      System.out.println(stu2.toString());
   }

}