import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.util.ArrayList;
import java.io.File;
import java.io.PrintWriter;
import java.io.FileNotFoundException;

// 16j
public class Tests {
	static ShoppingCartManager student = new ShoppingCartManager();
	private static ByteArrayOutputStream TOut;
	private static ByteArrayInputStream TIn;
	private static final PrintStream SOut = System.out;
	private static final InputStream SIn = System.in;
	private static int total = 0;
	private static int passed = 0;
	private static ArrayList<String> failed = new ArrayList<String>();

	public static void main(String[] args){
		simple();
		boolean verbose;
		try{
			verbose = !args[0].equals("simple");
		}
		catch (ArrayIndexOutOfBoundsException e){
			verbose = true;
		}
		if (verbose){
			System.out.printf("Passed %d out of %d tests.\n",passed, total);
			if (failed.size() > 0){
				System.out.println("Failed:");
				for (String i: failed){
					System.out.printf("\t* %s\n",i);
				}
			}
		}
	}

	public static void simple(){
		test1();
		test2();
		test3();
		test4();
		test5();
		test6();
		test7();
		test8();
		test9();
		test10();
		test11();
		test12();
		test13();
		test14();
		test15();
		System.out.printf("%d/%d\n",passed,total);
	}


	public static void test1(){
		total++;
		ItemToPurchase item = new ItemToPurchase("Bottled Water", "Deer Park, 12 oz.", 1, 10);
		if(item.getName()=="Bottled Water"&&
		item.getDescription()=="Deer Park, 12 oz."&&
		item.getPrice()==1&&item.getQuantity()==10){
			passed++;
		}
		else{
			failed.add("test1");
		}
	}

	public static void test2(){
		total++;
		String correct = "Volt color, Weightlifting shoes";
		ItemToPurchase item = new ItemToPurchase();
		item.setDescription(correct);
		String result = item.getDescription();
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test2");
		}
	}

	public static void test3(){
		total++;
		ShoppingCart cart = new ShoppingCart();
		if(cart.getCustomerName()=="none"&&
		cart.getDate().equals("January 1, 2016")){
			passed++;
		}
		else{
			failed.add("test3");
		}
	}

	public static void test4(){
		total++;
		ShoppingCart cart = new ShoppingCart("John Doe", "February 1, 2016");
		if(cart.getCustomerName()=="John Doe"&&
		cart.getDate().equals("February 1, 2016")){
			passed++;
		}
		else{
			failed.add("test4");
		}
	}

	public static void test5(){
		total++;
		int correct = 6;
		ShoppingCart cart = new ShoppingCart();
		ItemToPurchase item = new ItemToPurchase("none", "none", 1, 1);
		for(int i=0; i<6;i++){
			cart.addItem(item);
		}
		int result = cart.getNumItemsInCart();
		if (result == correct){
			passed++;
		}
		else{
			failed.add("test5");
		}
	}

	public static void test6(){
		total++;
		int correct = 9;
		ShoppingCart cart = new ShoppingCart();
		ItemToPurchase item1 = new ItemToPurchase("none", "none", 2, 4);
		ItemToPurchase item2 = new ItemToPurchase("none", "none", 1, 1);
		cart.addItem(item1);
		cart.addItem(item2);
		int result = cart.getCostOfCart();
		if (result == correct){
			passed++;
		}
		else{
			failed.add("test6");
		}
	}

	public static void test7(){
		total++;
		String correct = "Enter Customer's Name:\nEnter Today's Date:\n\nCustomer Name: John Doe\nToday's Date: February 1, 2016\n\n";
		String result = getOutput("John Doe\nFebruary 1, 2016\nq\n");
		result = result.substring(0,correct.length());
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test7");
		}
	}

	public static void test8(){
		total++;
		String correct = "Enter Customer's Name:\nEnter Today's Date:\n\nCustomer Name: John Doe\nToday's Date: February 1, 2016\n\n";
		correct += "MENU\na - Add item to cart\nd - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n\n";
		correct += "Choose an option:\nChoose an option:\nChoose an option:\n";
		String result = getOutput("John Doe\nFebruary 1, 2016\nf\ns\nq\n");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test8");
		}
	}

	public static void test9(){
		total++;
		String correct = "Enter Customer's Name:\nEnter Today's Date:\n\nCustomer Name: John Doe\nToday's Date: February 1, 2016\n\n";
		correct += "MENU\na - Add item to cart\nd - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n\n";
		correct += "Choose an option:\n";
		correct += "OUTPUT SHOPPING CART\nJohn Doe's Shopping Cart - February 1, 2016\nNumber of Items: 0\n\nSHOPPING CART IS EMPTY\n\nTotal: $0\n\n";
		correct += "MENU\na - Add item to cart\nd - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n\n";
		correct += "Choose an option:\n";
		String result = getOutput("John Doe\nFebruary 1, 2016\no\nq\n");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test9");
		}
	}

	public static void test10(){
		total++;
		String correct = "Enter Customer's Name:\nEnter Today's Date:\n\nCustomer Name: John Doe\nToday's Date: February 1, 2016\n\n";
		correct += "MENU\na - Add item to cart\nd - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n\n";
		correct += "Choose an option:\n";
		correct += "ADD ITEM TO CART\nEnter the item name:\nEnter the item description:\nEnter the item price:\nEnter the item quantity:\n\n";
		correct += "MENU\na - Add item to cart\nd - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n\n";
		correct += "Choose an option:\n";
		correct += "OUTPUT SHOPPING CART\nJohn Doe's Shopping Cart - February 1, 2016\nNumber of Items: 2\n\nNike Romaleos 2 @ $189 = $378\n\nTotal: $378\n\n";
		correct += "MENU\na - Add item to cart\nd - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n\n";
		correct += "Choose an option:\n";
		String result = getOutput("John Doe\nFebruary 1, 2016\na\nNike Romaleos\nVolt color, Weightlifting shoes\n189\n2\no\nq\n");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test10");
		}
	}

	public static void test11(){
		total++;
		setInput("John Doe\nFebruary 1, 2016\na\nNike Romaleos\nVolt color, Weightlifting shoes\n189\n2\nd\nSpectre DVD\nq\n");
		String correct = "Enter Customer's Name:\nEnter Today's Date:\n\nCustomer Name: John Doe\nToday's Date: February 1, 2016\n\n";
		correct += "MENU\na - Add item to cart\nd - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n\n";
		correct += "Choose an option:\n";
		correct += "ADD ITEM TO CART\nEnter the item name:\nEnter the item description:\nEnter the item price:\nEnter the item quantity:\n\n";
		correct += "MENU\na - Add item to cart\nd - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n\n";
		correct += "Choose an option:\n";
		correct += "REMOVE ITEM FROM CART\nEnter name of item to remove:\nItem not found in cart. Nothing removed.\n\n";
		correct += "MENU\na - Add item to cart\nd - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n\n";
		correct += "Choose an option:\n";
		String result = getOutput("John Doe\nFebruary 1, 2016\na\nNike Romaleos\nVolt color, Weightlifting shoes\n189\n2\nd\nSpectre DVD\nq\n");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test11");
		}
	}

	public static void test12(){
		total++;
		String correct = "Enter Customer's Name:\nEnter Today's Date:\n\nCustomer Name: John Doe\nToday's Date: February 1, 2016\n\n";
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
		String result = getOutput("John Doe\nFebruary 1, 2016\na\nNike Romaleos\nVolt color, Weightlifting shoes\n189\n2\na\nChocolate Chips\nSemi-sweet\n3\n5\na\nPowerbeats 2 Headphones\nBluetooth headphones\n128\n1\nd\nChocola    te Chips\no\nq\n");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test12");
		}
	}

	public static void test13(){
		total++;
		String correct = "CHANGE ITEM QUANTITY\nEnter the item name:\nEnter the new quantity:\nItem not found in cart. Nothing modified.\n\n";
		correct += "MENU\na - Add item to cart\nd - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n\n";
		correct += "Choose an option:\n";
		String result = getOutput("John Doe\nFebruary 1, 2016\na\nNike Romaleos\nVolt color, Weightlifting shoes\n189\n2\na\nChocolate Chips\nSemi-sweet\n3\n5\na\nPowerbeats 2 Headphones\nBluetooth headphones\n128\n1\nc\nThe    rmos Stainless Steel King\n5\nq\n");
		result = result.substring(result.length()-correct.length(),result.length());
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test13");
		}
	}

	public static void test14(){
		total++;
		String correct = "OUTPUT SHOPPING CART\nJohn Doe's Shopping Cart - February 1, 2016\nNumber of Items: 9\n\nNike Romaleos 3 @ $189 = $567\nChocolate Chips 5 @ $3 = $15\nPowerbeats 2 Headphones 1 @ $128 = $128\n\nTotal: $710\n\n";
		correct += "MENU\na - Add item to cart\nd - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n\n";
		correct += "Choose an option:\n";
		String result = getOutput("John Doe\nFebruary 1, 2016\na\nNike Romaleos\nVolt color, Weightlifting shoes\n189\n2\na\nChocolate Chips\nSemi-sweet\n3\n5\na\nPowerbeats 2 Headphones\nBluetooth headphones\n128\n1\nc\nNike Ro    maleos\n3\no\nq\n");
		result = result.substring(result.length()-correct.length(),result.length());
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test14");
		}
	}

	public static void test15(){
		total++;
		String correct = "OUTPUT ITEMS' DESCRIPTIONS\nJohn Doe's Shopping Cart - February 1, 2016\n\nItem Descriptions\nNike Romaleos: Volt color, Weightlifting shoes\nChocolate Chips: Semi-sweet\nPowerbeats 2 Headphones: Bluetooth headphones\n\n";
		correct += "MENU\na - Add item to cart\nd - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n\n";
		correct += "Choose an option:\n";
		String result = getOutput("John Doe\nFebruary 1, 2016\na\nNike Romaleos\nVolt color, Weightlifting shoes\n189\n2\na\nChocolate Chips\nSemi-sweet\n3\n5\na\nPowerbeats 2 Headphones\nBluetooth headphones\n128\n1\ni\nq\n    ");
		result = result.substring(result.length()-correct.length(),result.length());
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test15");
		}
	}

	//no hidden tests for 16

	//Set up methods
	 public static void setOutput(){
	 	TOut = new ByteArrayOutputStream();
		System.setOut(new PrintStream(TOut));
	}
	private static void setInput(String data){
		TIn = new ByteArrayInputStream(data.getBytes());
		System.setIn(TIn);
	}
	private static String getOutput(String input){
		setOutput();
		setInput(input);
		student.main(null);
		String result = TOut.toString();
		restoreSystem();
		return result;
	}
	public static void restoreSystem(){
		System.setOut(SOut);
		System.setIn(SIn);
	}
	public static void toFile(String correct, String result){
		try{
			File f;
			PrintWriter p;
			String[] a = {"correct","result"};
			String[] args = {correct,result};
			for (int i = 0; i<2;i++){
				f = new File(a[i]+".txt");
				p = new PrintWriter(f);
				p.print(args[i]);
				p.close();
			}
		}
		catch (FileNotFoundException e){
			System.out.println("Couldn't create files.");
			System.out.println(e);
		}
	}
}
