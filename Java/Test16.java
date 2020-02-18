import java.io.*;

public class Test16 {
  static ShoppingCartManager student = new ShoppingCartManager();
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
    ItemToPurchase item = new ItemToPurchase("Bottled Water", "Deer Park, 12 oz.", 1, 10);
    if(item.getName()=="Bottled Water"&&
    item.getDescription()=="Deer Park, 12 oz."&&
    item.getPrice()==1&&item.getQuantity()==10){
      score++;
    }
    //test2
    total++;
    item = new ItemToPurchase();
    item.setDescription("Volt color, Weightlifting shoes");
    String result = item.getDescription();
    String correct = "Volt color, Weightlifting shoes";
    if (result.equals(correct)){
      score++;
    }
    //test3
    total++;
    ShoppingCart cart = new ShoppingCart();
    if(cart.getCustomerName()=="none"&&
    cart.getDate().equals("January 1, 2016")){
      score++;
    }
    //test4
    total++;
    cart = new ShoppingCart("John Doe", "February 1, 2016");
    if(cart.getCustomerName()=="John Doe"&&
    cart.getDate().equals("February 1, 2016")){
      score++;
    }
    //test5
    total++;
    cart = new ShoppingCart();
    item = new ItemToPurchase();
    item.setQuantity(1);
    for(int i=0; i<6;i++){
      cart.addItem(item);
    }
    int r = cart.getNumItemsInCart();
    if (r==6){
      score++;
    }
    //test6
    total++;
    cart = new ShoppingCart();
    ItemToPurchase item1 = new ItemToPurchase();
    ItemToPurchase item2 = new ItemToPurchase();

    item1.setPrice(2);
    item1.setQuantity(4);
    cart.addItem(item1);

    item2.setPrice(1);
    item2.setQuantity(1);
    cart.addItem(item2);

    r = cart.getCostOfCart();
    if (r==9){
      score++;
    }
    //test7
    setOutput();
    total++;
    setInput("John Doe\nFebruary 1, 2016\nq\n");
    student.main(args);
    correct = "Enter Customer's Name:\nEnter Today's Date:\n\nCustomer Name: John Doe\nToday's Date: February 1, 2016\n\n";
    result = getOutput().substring(0,correct.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test8
    setOutput();
    total++;
    setInput("John Doe\nFebruary 1, 2016\nf\ns\nq\n");
    student.main(args);
    correct = "Enter Customer's Name:\nEnter Today's Date:\n\nCustomer Name: John Doe\nToday's Date: February 1, 2016\n\n";
    correct += "MENU\na - Add item to cart\nd - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n\n";
    correct += "Choose an option:\nChoose an option:\nChoose an option:\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test9
    setOutput();
    total++;
    setInput("John Doe\nFebruary 1, 2016\no\nq\n");
    student.main(args);
    correct = "Enter Customer's Name:\nEnter Today's Date:\n\nCustomer Name: John Doe\nToday's Date: February 1, 2016\n\n";
    correct += "MENU\na - Add item to cart\nd - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n\n";
    correct += "Choose an option:\n";
    correct += "OUTPUT SHOPPING CART\nJohn Doe's Shopping Cart - February 1, 2016\nNumber of Items: 0\n\nSHOPPING CART IS EMPTY\n\nTotal: $0\n\n";
    correct += "MENU\na - Add item to cart\nd - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n\n";
    correct += "Choose an option:\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test10
    setOutput();
    total++;
    setInput("John Doe\nFebruary 1, 2016\na\nNike Romaleos\nVolt color, Weightlifting shoes\n189\n2\no\nq\n");
    student.main(args);
    correct = "Enter Customer's Name:\nEnter Today's Date:\n\nCustomer Name: John Doe\nToday's Date: February 1, 2016\n\n";
    correct += "MENU\na - Add item to cart\nd - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n\n";
    correct += "Choose an option:\n";
    correct += "ADD ITEM TO CART\nEnter the item name:\nEnter the item description:\nEnter the item price:\nEnter the item quantity:\n\n";
    correct += "MENU\na - Add item to cart\nd - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n\n";
    correct += "Choose an option:\n";
    correct += "OUTPUT SHOPPING CART\nJohn Doe's Shopping Cart - February 1, 2016\nNumber of Items: 2\n\nNike Romaleos 2 @ $189 = $378\n\nTotal: $378\n\n";
    correct += "MENU\na - Add item to cart\nd - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n\n";
    correct += "Choose an option:\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test11
    setOutput();
    total++;
    setInput("John Doe\nFebruary 1, 2016\na\nNike Romaleos\nVolt color, Weightlifting shoes\n189\n2\nd\nSpectre DVD\nq\n");
    student.main(args);
    correct = "Enter Customer's Name:\nEnter Today's Date:\n\nCustomer Name: John Doe\nToday's Date: February 1, 2016\n\n";
    correct += "MENU\na - Add item to cart\nd - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n\n";
    correct += "Choose an option:\n";
    correct += "ADD ITEM TO CART\nEnter the item name:\nEnter the item description:\nEnter the item price:\nEnter the item quantity:\n\n";
    correct += "MENU\na - Add item to cart\nd - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n\n";
    correct += "Choose an option:\n";
    correct += "REMOVE ITEM FROM CART\nEnter name of item to remove:\nItem not found in cart. Nothing removed.\n\n";
    correct += "MENU\na - Add item to cart\nd - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n\n";
    correct += "Choose an option:\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test12
    setOutput();
    total++;
    setInput("John Doe\nFebruary 1, 2016\na\nNike Romaleos\nVolt color, Weightlifting shoes\n189\n2\na\nChocolate Chips\nSemi-sweet\n3\n5\na\nPowerbeats 2 Headphones\nBluetooth headphones\n128\n1\nd\nChocolate Chips\no\nq\n");
    student.main(args);
    correct = "Enter Customer's Name:\nEnter Today's Date:\n\nCustomer Name: John Doe\nToday's Date: February 1, 2016\n\n";
    correct += "MENU\na - Add item to cart\nd - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n\n";
    correct += "Choose an option:\n";
    correct += "ADD ITEM TO CART\nEnter the item name:\nEnter the item description:\nEnter the item price:\nEnter the item quantity:\n\n";
    correct += "MENU\na - Add item to cart\nd - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n\n";
    correct += "Choose an option:\n";
    correct += "ADD ITEM TO CART\nEnter the item name:\nEnter the item description:\nEnter the item price:\nEnter the item quantity:\n\n";
    correct += "MENU\na - Add item to cart\nd - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n\n";
    correct += "Choose an option:\n";
    correct += "ADD ITEM TO CART\nEnter the item name:\nEnter the item description:\nEnter the item price:\nEnter the item quantity:\n\n";
    correct += "MENU\na - Add item to cart\nd - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n\n";
    correct += "Choose an option:\n";
    correct += "REMOVE ITEM FROM CART\nEnter name of item to remove:\n\n";
    correct += "MENU\na - Add item to cart\nd - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n\n";
    correct += "Choose an option:\n";
    correct += "OUTPUT SHOPPING CART\nJohn Doe's Shopping Cart - February 1, 2016\nNumber of Items: 3\n\nNike Romaleos 2 @ $189 = $378\nPowerbeats 2 Headphones 1 @ $128 = $128\n\nTotal: $506\n\n";
    correct += "MENU\na - Add item to cart\nd - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n\n";
    correct += "Choose an option:\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test13
    setOutput();
    total++;
    setInput("John Doe\nFebruary 1, 2016\na\nNike Romaleos\nVolt color, Weightlifting shoes\n189\n2\na\nChocolate Chips\nSemi-sweet\n3\n5\na\nPowerbeats 2 Headphones\nBluetooth headphones\n128\n1\nc\nThermos Stainless Steel King\n5\nq\n");
    student.main(args);
    correct = "CHANGE ITEM QUANTITY\nEnter the item name:\nEnter the new quantity:\nItem not found in cart. Nothing modified.\n\n";
    correct += "MENU\na - Add item to cart\nd - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n\n";
    correct += "Choose an option:\n";
    result = getOutput();
    result = result.substring(result.length()-correct.length(),result.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test14
    setOutput();
    total++;
    setInput("John Doe\nFebruary 1, 2016\na\nNike Romaleos\nVolt color, Weightlifting shoes\n189\n2\na\nChocolate Chips\nSemi-sweet\n3\n5\na\nPowerbeats 2 Headphones\nBluetooth headphones\n128\n1\nc\nNike Romaleos\n3\no\nq\n");
    student.main(args);
    correct = "OUTPUT SHOPPING CART\nJohn Doe's Shopping Cart - February 1, 2016\nNumber of Items: 9\n\nNike Romaleos 3 @ $189 = $567\nChocolate Chips 5 @ $3 = $15\nPowerbeats 2 Headphones 1 @ $128 = $128\n\nTotal: $710\n\n";
    correct += "MENU\na - Add item to cart\nd - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n\n";
    correct += "Choose an option:\n";
    result = getOutput();
    result = result.substring(result.length()-correct.length(),result.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test15
    setOutput();
    total++;
    setInput("John Doe\nFebruary 1, 2016\na\nNike Romaleos\nVolt color, Weightlifting shoes\n189\n2\na\nChocolate Chips\nSemi-sweet\n3\n5\na\nPowerbeats 2 Headphones\nBluetooth headphones\n128\n1\ni\nq\n");
    student.main(args);
    correct = "OUTPUT ITEMS' DESCRIPTIONS\nJohn Doe's Shopping Cart - February 1, 2016\n\nItem Descriptions\nNike Romaleos: Volt color, Weightlifting shoes\nChocolate Chips: Semi-sweet\nPowerbeats 2 Headphones: Bluetooth headphones\n\n";
    correct += "MENU\na - Add item to cart\nd - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n\n";
    correct += "Choose an option:\n";
    result = getOutput();
    result = result.substring(result.length()-correct.length(),result.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //no hidden tests for 16
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
