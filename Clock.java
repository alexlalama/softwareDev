/**
 * Portray a clock
 *@author Alex Lalama
 *@version 05122025
 **/
public class Clock
{

   // Attributes
   private int currentHour;
   private int currentMinute;
   private String am_or_pm;
   
   public Clock(int hour, int minute, String amPm)
   {
      
      currentHour = hour;
      currentMinute = minute;
      am_or_pm = amPm;
   
   }
   public static void main(String[] args)
   {
      Clock clock = new Clock(8,25,"AM");
      clock.print();
      
      clock.setHour(9);
      clock.setMinute(14);
      clock.setAm_Pm("PM");
      System.out.println("Updated hour: " + clock.getCurrentHour());
      System.out.println("Updated minute: " + clock.getCurrentMinute());
      System.out.println("Updated AM/PM: " + clock.getAm_or_pm());
      clock.print();
  }
   
   /**
    Access Modifiers
    */
    
   // Get the current time
  
   public int getCurrentHour()
   {
      return currentHour;
   
   }
   /**
    Get Current Minute
   **/
   public int getCurrentMinute()
   {
      return currentMinute;
   
   }
   /**
    Get Current AM or PM
    **/
   public String getAm_or_pm()
   {
      return am_or_pm;
   
   }

   public void print()
   {
      System.out.println(currentHour + ":" + currentMinute + " " + am_or_pm);
   }
   
   public void setHour(int hour)
   {
      currentHour = hour;
   }
   public void setMinute(int minute)
   {
      currentMinute = minute;
   }
   public void setAm_Pm(String amPm)
   {
      am_or_pm = amPm;
   }
   // Set the time of day
   // Set it to a 12-hour or 24-hour setting
   
   
}