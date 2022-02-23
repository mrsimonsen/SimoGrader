import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.util.ArrayList;
import java.io.File;
import java.io.PrintWriter;
import java.io.FileNotFoundException;

// 13j
public class Tests {
	static TextAnalyzer student = new TextAnalyzer();
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
		hidden1();
		hidden2();
		System.out.printf("%d/%d\n",passed,total);
	}

	public static void test1(){
		total++;
		String correct = "Enter a sentence or phrase:\n\nYou entered: The only thing we have to fear is fear itself.\n";
		String result = getOutput("The only thing we have to fear is fear itself.\n");
		result = result.substring(0,correct.length());
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test1");
		}
	}

	public static void test2(){
		total++;
		int correct = 36;
		int result = student.getNumOfCharacters("The only thing we have to fear is fear itself.");
		if (result == correct){
			passed++;
		}
		else{
			failed.add("test2");
		}
	}

	public static void test3(){
		total++;
		int correct = 35;
		int result = student.getNumOfCharacters("The rain in Spain stays mainly in the plain.");
		if (result == correct){
			passed++;
		}
		else{
			failed.add("test3");
		}
	}

	public static void test4(){
		total++;
		String correct = "Enter a sentence or phrase:\n\nYou entered: The only thing we have to fear is fear itself.\n";
		correct += "\nNumber of characters: 36\n";
		String result = getOutput("The only thing we have to fear is fear itself.\n");
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
		String correct = "Enter a sentence or phrase:\n\nYou entered: The only thing we have to fear is fear itself.\n";
		correct += "\nNumber of characters: 36\n";
		correct += "String with no whitespace: Theonlythingwehavetofearisfearitself.\n";
		String result = getOutput("The only thing we have to fear is fear itself.\n");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test5");
		}
	}

	public static void test6(){
		total++;
		String correct = "Enter a sentence or phrase:\n\nYou entered: The rain in Spain stays mainly in the plain.\n";
		correct += "\nNumber of characters: 35\n";
		correct += "String with no whitespace: TheraininSpainstaysmainlyintheplain.\n";
		String result = getOutput("The rain in Spain stays mainly in the plain.\n");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test6");
		}
	}

	public static void hidden1(){
		total++;
		String correct = "Enter a sentence or phrase:\n\nYou entered: May the Force be with you!\n";
		correct += "\nNumber of characters: 20\n";
		correct += "String with no whitespace: MaytheForcebewithyou!\n";
		String result = getOutput("May the Force be with you!\n");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("hidden1");
		}
	}

	public static void hidden2(){
		total++;
		String correct = "Enter a sentence or phrase:\n\nYou entered: Simonsen\n";
		correct += "\nNumber of characters: 8\n";
		correct += "String with no whitespace: Simonsen\n";
		String result = getOutput("Simonsen\n");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("hidden2");
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
