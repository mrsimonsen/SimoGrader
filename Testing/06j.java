import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.util.ArrayList;
import java.io.File;
import java.io.PrintWriter;
import java.io.FileNotFoundException;

// 06j
public class Tests {
	static DrawRightTriangle student = new DrawRightTriangle();
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
		hidden1();
		System.out.printf("%d/%d\n",passed,total);
	}

	public static void test1(){
		total++;
		String correct = "Enter a character:\nEnter triangle height:\n";
		correct += "\n@ \n@ @ \n@ @ @ \n";
		String result = getOutput("@ 3");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test1");
		}

	public static void test2(){
		total++;
		String correct = "Enter a character:\nEnter triangle height:\n";
		correct += "\n% \n% % \n% % % \n% % % % \n% % % % % \n";
		String result = getOutput("% 5");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test2");
		}
	}

	public static void test3(){
		total++;
		String correct = "Enter a character:\nEnter triangle height:\n";
		correct += "\nm \nm m \nm m m \nm m m m \n";
		String result = getOutput("m 4");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test3");
		}
	}

	public static void hidden1(){
		total++;
		String correct = "Enter a character:\nEnter triangle height:\n";
		correct += "\nx \nx x \nx x x \nx x x x \nx x x x x \nx x x x x x \nx x x x x x x \nx x x x x x x x \nx x x x x x x x x \nx x x x x x x x x x \n";
		String result = getOutput("x 10");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("hidden1");
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