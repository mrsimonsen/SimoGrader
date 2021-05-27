import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.util.ArrayList;
import java.io.File;
import java.io.PrintWriter;
import java.io.FileNotFoundException;

// 15j
public class Tests {
	static ShoppingCartPrinter student = new ShoppingCartPrinter();
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
		hidden1();
		System.out.printf("%d/%d\n",passed,total);
	}

	public static void test1(){
		total++;
		String correct = "Chocolate Chips";
		ItemToPurchase item = new ItemToPurchase();
		item.setName("Chocolate Chips");
		String result = item.getName();
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test1");
		}
	}

	public static void test2(){
		total++;
		int correct = 3;
		item = new ItemToPurchase();
		item.setPrice(3);
		int result = item.getPrice();
		if (result == correct){
			passed++;
		}
		else{
			failed.add("test2");
		}
	}

	public static void test3(){
		total++;
		int correct = 4;
		item = new ItemToPurchase();
		item.setQuantity(4);
		int result = item.getQuantity();
		if (result == correct){
			passed++;
		}
		else{
			failed.add("test3");
		}
	}

	public static void test4(){
		total++;
		String correct = "Item 1\nEnter the item name:\nEnter the item price:\nEnter the item quantity:\n";
		correct += "\nItem 2\nEnter the item name:\nEnter the item price:\nEnter the item quantity:\n";
		String result = getOutput("Chocolate Chips\n3\n1\nBottled Water\n1\n10\n");
		result = result.substring(0,correct.length());
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test4");
		}
	}

	public static void test5(){
		total++;
		String correct = "Item 1\nEnter the item name:\nEnter the item price:\nEnter the item quantity:\n";
		correct += "\nItem 2\nEnter the item name:\nEnter the item price:\nEnter the item quantity:\n";
		correct += "\nTOTAL COST\nChocolate Chips 1 @ $3 = $3\n";
		correct += "Bottled Water 10 @ $1 = $10\n";
		correct += "\nTotal: $13\n";
		String result = getOutput("Chocolate Chips\n3\n1\nBottled Water\n1\n10\n");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test5");
		}
	}

	public static void hidden1(){
		total++;
		String correct = "Item 1\nEnter the item name:\nEnter the item price:\nEnter the item quantity:\n";
		correct += "\nItem 2\nEnter the item name:\nEnter the item price:\nEnter the item quantity:\n";
		correct += "\nTOTAL COST\nImperal Logo Sticker 2 @ $20 = $40\n";
		correct += "R2-D2 Bust 3 @ $31 = $93\n";
		correct += "\nTotal: $133\n";
		String result = getOutput("Imperal Logo Sticker\n20\n2\nR2-D2 Bust\n31\n3\n");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("hidden1");
		}
	}

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
