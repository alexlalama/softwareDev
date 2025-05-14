public class Lab01Ex2
{

   public static void main(String[] args)
   
   {
 
      Account account1 = new Account();
      Account account2 = new Account(); 
      account1.initialize("Jane");
      System.out.print("Account: ");
      account1.print();
      account1.deposit(100);
      account1.print();
      account1.withdraw(40);
      account1.print();
      account2.initialize("Fred");
      account2.print();
      account2.deposit(200);
      account2.print();
      account2.withdraw(125);
      account2.print();
      Account account3 = new Account();
      account3.initialize("Person");
      account3.deposit(50);
      account3.print();

      account2.deposit(60);
      account2.print();

      account1.withdraw(20);
      account1.print();


  }

}