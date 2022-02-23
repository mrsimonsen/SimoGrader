import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.util.ArrayList;
import java.io.File;
import java.io.PrintWriter;
import java.io.FileNotFoundException;

// 18j
public class Tests {
	static ParseStrings student = new ParseStrings();
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
		hidden1();
		System.out.printf("%d/%d\n",passed,total);
	}

	public static void test1(){
		total++;
		String correct = "Enter input string:\n";
		String result = getOutput("John, Simonsen\nq\n");
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
		String correct = "Enter input string:\nError: No comma in string.\n\nEnter input string:\nError: No comma in string.\n\nEnter input string:\nError: No comma in string.\n\nEnter input string:\n";
		String result = getOutput("John Simonsen\nJohnSimonsen\nJohn  Simonsen\nq\n");
		result = result.substring(0,correct.length());
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test2");
		}
	}

	public static void test3(){
		total++;
		String correct = "Enter input string:\nFirst word: John\nSecond word: Simonsen\n";
		String result = getOutput("John, Simonsen\nq\n").substring(0,correct.length());
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test3");
		}
	}

	public static void test4(){
		total++;
		String correct = "Enter input string:\nFirst word: John\nSecond word: Simonsen\n\n";
		correct += "Enter input string:\nFirst word: Luke\nSecond word: Skywalker\n\n";
		correct += "Enter input string:\nFirst word: Layton\nSecond word: UT\n\n";
		correct += "Enter input string:\n";
		String result = getOutput("John, Simonsen\nLuke , Skywalker\nLayton,UT\nq\n");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test4");
		}
	}

	public static void hidden1(){
		total++;
		String correct = "Enter input string:\nFirst word: Leia\nSecond word: Organa\n\n";
		correct += "Enter input string:\nFirst word: Darth\nSecond word: Vader\n\n";
		correct += "Enter input string:\nFirst word: Death\nSecond word: Star\n\n";
		correct += "Enter input string:\n";
		String result = getOutput("Leia , Organa\nDarth,Vader\nDeath, Star\nq\n");
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
