import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.util.ArrayList;
import java.io.File;
import java.io.PrintWriter;
import java.io.FileNotFoundException;

// 12j
public class Tests {
	static DiceStats student = new DiceStats();
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
		boolean correct = true;
		boolean result = student.cont(1);
		if (result == correct){
			passed++;
		}
		else{
			failed.add("test1");
		}
	}

	public static void test2(){
		total++;
		boolean correct = false;
		boolean result = student.cont(0);
		if (result == correct){
			passed++;
		}
		else{
			failed.add("test2");
		}
	}

	public static void test3(){
		total++;
		boolean correct = true;
		boolean result = student.cont(10);
		if (result == correct){
			passed++;
		}
		else{
			failed.add("test3");
		}
	}

	public static void test4(){
		total++;
		String star = "*\n";
		String correct = "Dice roll histogram:\n\n";
		correct += "2:  "+star;
		correct += "3:  "+star;
		correct += "4:  "+star;
		correct += "5:  "+star;
		correct += "6:  "+star;
		correct += "7:  "+star;
		correct += "8:  "+star;
		correct += "9:  "+star;
		correct += "10: "+star;
		correct += "11: "+star;
		correct += "12: "+star;
		int[] total = {1,1,1,1,1,1,1,1,1,1,1};
		String result = student.histogram(total);
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test4");
		}
	}

	public static test5(){
		total++;
		String star = "****\n";
		String correct = "Dice roll histogram:\n\n";
		correct += "2:  "+star;
		correct += "3:  "+star;
		correct += "4:  "+star;
		correct += "5:  "+star;
		correct += "6:  "+star;
		correct += "7:  "+star;
		correct += "8:  "+star;
		correct += "9:  "+star;
		correct += "10: "+star;
		correct += "11: "+star;
		correct += "12: "+star;
		int[] total = {4,4,4,4,4,4,4,4,4,4,4};
		String result = student.histogram(total);
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test5");
		}
	}

public static void test6(){
		total++;
		String correct = "Dice roll histogram:\n\n";
		correct += "2:  **\n";
		correct += "3:  ***\n";
		correct += "4:  *****\n";
		correct += "5:  ***\n";
		correct += "6:  ***\n";
		correct += "7:  ***\n";
		correct += "8:  *****\n";
		correct += "9:  ********\n";
		correct += "10: ****\n";
		correct += "11: *\n";
		correct += "12: ***\n";
		int[] total = {2,3,5,3,3,3,5,8,4,1,3};
		String result = student.histogram(total);
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test6");
		}
	}

	public static void hidden1(){
		total++;
		String correct = "Dice roll histogram:\n\n";
		correct += "2:  *\n";
		correct += "3:  **\n";
		correct += "4:  ***\n";
		correct += "5:  ****\n";
		correct += "6:  *****\n";
		correct += "7:  ******\n";
		correct += "8:  *******\n";
		correct += "9:  ********\n";
		correct += "10: *********\n";
		correct += "11: **********\n";
		correct += "12: ***********\n";
		int[] total = {1,2,3,4,5,6,7,8,9,10,11};
		String result = student.histogram(total);
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("hidden1");
		}
	}

	public static void hidden2(){
		total++;
		int[] total6 = {11,10,9,8,7,6,5,4,3,2,1};
		String correct = "Dice roll histogram:\n\n";
		correct += "2:  ***********\n";
		correct += "3:  **********\n";
		correct += "4:  *********\n";
		correct += "5:  ********\n";
		correct += "6:  *******\n";
		correct += "7:  ******\n";
		correct += "8:  *****\n";
		correct += "9:  ****\n";
		correct += "10: ***\n";
		correct += "11: **\n";
		correct += "12: *\n";
		int[] total = {11,10,9,8,7,6,5,4,3,2,1};
		String result = student.histogram(total);
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
