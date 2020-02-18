import java.io.*;

public class Test15 {
  static ShoppingCartPrinter student = new ShoppingCartPrinter();
  static private ByteArrayOutputStream TOut;
  static private ByteArrayInputStream TIn;
  static private final PrintStream SOut = System.out;
  static private final InputStream SIn = System.in;
  static String[] args = {};

  public static void main(String[] args){
    System.out.println(tests());
  }

  public static String tests(){
    int total = 0;
    int score = 0;

    //test1
    total++;
    ItemToPurchase item = new ItemToPurchase();
    item.setName("Chocolate Chips");
    String correct = "Chocolate Chips";
    String result = item.getName();
    if (result.equals(correct)){
      score++;
    }
    //test2
    total++;
    item = new ItemToPurchase();
    item.setPrice(3);
    int r = item.getPrice();
    if (r==3){
      score++;
    }
    //test3
    total++;
    item = new ItemToPurchase();
    item.setQuantity(4);
    r = item.getQuantity();
    if (r==4){
      score++;
    }
    //test4
    setOutput();
    total++;
    setInput("Chocolate Chips\n3\n1\nBottled Water\n1\n10\n");
    student.main(args);
    correct = "Item 1\nEnter the item name:\nEnter the item price:\nEnter the item quantity:\n";
    correct += "\nItem 2\nEnter the item name:\nEnter the item price:\nEnter the item quantity:\n";
    result = getOutput().substring(0,correct.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test5
    setOutput();
    total++;
    setInput("Chocolate Chips\n3\n1\nBottled Water\n1\n10\n");
    student.main(args);
    correct = "Item 1\nEnter the item name:\nEnter the item price:\nEnter the item quantity:\n";
    correct += "\nItem 2\nEnter the item name:\nEnter the item price:\nEnter the item quantity:\n";
    correct += "\nTOTAL COST\nChocolate Chips 1 @ $3 = $3\n";
    correct += "Bottled Water 10 @ $1 = $10\n";
    correct += "\nTotal: $13\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }

    //hidden test
    setOutput();
    total++;
    setInput("Imperal Logo Sticker\n20\n2\nR2-D2 Bust\n31\n3\n");
    student.main(args);
    correct = "Item 1\nEnter the item name:\nEnter the item price:\nEnter the item quantity:\n";
    correct += "\nItem 2\nEnter the item name:\nEnter the item price:\nEnter the item quantity:\n";
    correct += "\nTOTAL COST\nImperal Logo Sticker 2 @ $20 = $40\n";
    correct += "R2-D2 Bust 3 @ $31 = $93\n";
    correct += "\nTotal: $133\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }

    //testing complete
    String rep = ""+ score +"/"+total;
    return rep;
  }

  //Set up methods
  static public void setOutput(){
    TOut = new ByteArrayOutputStream();
    System.setOut(new PrintStream(TOut));
  }
  private static void setInput(String data){
  TIn = new ByteArrayInputStream(data.getBytes());
  System.setIn(TIn);
  }
  static private String getOutput(){
    return TOut.toString();
  }
  static public void restoreSystem(){
    System.setOut(SOut);
    System.setIn(SIn);
  }
}
