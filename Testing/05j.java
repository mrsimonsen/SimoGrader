import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.util.ArrayList;
import java.io.File;
import java.io.PrintWriter;
import java.io.FileNotFoundException;

// 05j
public class Tests {
	static TextMsgExpander student = new TextMsgExpander();
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
		String correct = "Enter text:\nYou entered: IDK how that happened. TTYL.\n";
		String result = getOutput("IDK how that happened. TTYL.");
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
		String correct = "Enter text:\nYou entered: IDK how that happened. TTYL.\n";
		correct += "\nReplaced \"IDK\" with \"I don't know\".\nReplaced \"TTYL\" with \"talk to you later\".\n";
		correct += "\nExpanded: I don't know how that happened. talk to you later.\n";
		String result = getOutput("IDK how that happened. TTYL.");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test2");
		}
	}

	public static void test3(){
		total++;
		String correct = "Enter text:\nYou entered: I'll fix it. JK, you know IDK how.\n";
		correct += "\nReplaced \"IDK\" with \"I don't know\".\nReplaced \"JK\" with \"just kidding\".\n";
		correct += "\nExpanded: I'll fix it. just kidding, you know I don't know how.\n";
		String result = getOutput("I'll fix it. JK, you know IDK how.");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test3");
		}
	}

	public static void test4(){
		total++;
		String correct = "Enter text:\nYou entered: Your bff, my BFF, and her BFF are all there.\n";
		correct += "\nReplaced \"BFF\" with \"best friend forever\".\n";
		correct += "\nExpanded: Your bff, my best friend forever, and her best friend forever are all there.\n";
		String result = getOutput("Your bff, my BFF, and her BFF are all there.");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test4");
		}
	}

	public static void hidden1(){
		total++;
		String correct = "Enter text:\nYou entered: JK, IDK if TMI BFF. TTYL\n";
		correct = correct += "\nReplaced \"BFF\" with \"best friend forever\".\nReplaced \"IDK\" with \"I don't know\".\nReplaced \"JK\" with \"just kidding\".\nReplaced \"TMI\" with \"too much information\".\nReplaced \"TTYL\" with \"talk to you later\".\n";
		correct += "\nExpanded: just kidding, I don't know if too much information best friend forever. talk to you later\n";
		String result = getOutput("JK, IDK if TMI BFF. TTYL");
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
