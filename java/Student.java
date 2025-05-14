/**
 * Student - class to represent a Student
 *@author Alex Lalama
 *@version 05122025
 */
public class Student
{
   //Attributes
   private String firstName;
   private String lastName;
   private int studentId;
   private double gpa;
   public Student(String _firstName, String _lastName,int _studentId, double _gpa)
   {
         firstName = _firstName;
         lastName = _lastName;
         studentId = _studentId;
         gpa = _gpa;
   }
    
   // Access Modifiers
   public String getFirstName()
   {
     return firstName;
   }
   public String getLastName()
   {
     return lastName;
   }
   public int getStudentId()
   {
     return studentId;
   }
   public double getGpa()
   {
     return gpa;
   } 
   // Setters
   
   public void setFirstName(String _firstName)
   {
      firstName = _firstName;   
   }
   public void setLastName(String _lastName)
   {
      lastName = _lastName;

   } 
   public void setStudentId(int _studentId)
   {
      studentId = _studentId;

   }
   
   public void setGpa(double _gpa)
   {
      gpa = _gpa;

   }
   
   public void print()
   {
   
   }
   public void setNewStudentId()
   {
      studentId = studentId + 5;
   }
   public int getNewStudentId()
   {
      return studentId;
   }
   public String toString()
   {
      String studentInfo = "Student: " + getFirstName() + " " + getLastName() + " " +
      getStudentId() + " " + getGpa();
      return studentInfo;
   }
}