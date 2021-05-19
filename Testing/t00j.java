import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.util.ArrayList;
import java.io.File;
import java.io.PrintWriter;
import java.io.FileNotFoundException;

public class t00j {
	static HelloWorld student = new HelloWorld();
	private static ByteArrayOutputStream TOut;
	private static ByteArrayInputStream TIn;
	private static final PrintStream SOut = System.out;
	private static final InputStream SIn = System.in;
	private static int testCount = 0;
	private static int passed = 0;
	
	public static void main(String[] args){
		ArrayList<String> failed = new ArrayList<String>();
		if (! test1()){
			failed.add("test1");
		}
		System.out.printf("Passed %d out of %d tests.\n",passed, testCount);
		System.out.println("Failed:");
		for (String i: failed){
			System.out.printf("\t* %s\n",i);
		}
	}
	
	public String runner(){
		test1();
		return ""+passed+"/"+testCount;
	}

	public static boolean test1(){
		testCount++;
		String correct = "Hello World!\n";
		String result = getOutput("");
		if (result.equals(correct)){
			passed++;
			return true;
		}
		return false;
	}

	//no hidden tests for assignment 00

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
