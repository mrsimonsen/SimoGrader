import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.util.ArrayList;
import java.io.File;
import java.io.PrintWriter;
import java.io.FileNotFoundException;
import java.util.Arrays;

// 08j
public class Tests {
 	static PeopleWeights student = new PeopleWeights();
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
		testArray1();
		test2();
		testArray2();
		test3();
		test4();
		test5();
		hidden1();
		hidden2();
		System.out.printf("%d/%d\n",passed,total);
	}

	public static void test1(){
		total++;
		String correct = "Enter weight 1:\nEnter weight 2:\nEnter weight 3:\nEnter weight 4:\nEnter weight 5:\n";
		correct += "You entered: 236.0 89.5 142.0 166.3 93.0 \n";
		String result = getOutput("236.0 89.5 142.0 166.3 93.0");
		result = result.substring(0,correct.length());
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test1");
		}
	}

	static public void testArray1(){
		total++;
		double[] correct = {236,89.5,142.0,166.3,93};
		String input = "236.0 89.5 142.0 166.3 93.0";
		getOutput(input);
		double[] result = student.userWeights;
		if (Arrays.equals(result, correct)){
			passed++;
		}
		else{
			failed.add("testArray1");
		}
	}

	public static void test2(){
		total++;
		String correct = "Enter weight 1:\nEnter weight 2:\nEnter weight 3:\nEnter weight 4:\nEnter weight 5:\n";
		correct += "You entered: 123.4 56.0 98.0 174.0 215.8 \n";
		String result = getOutput("123.4 56.0 98.0 174.0 215.8");
		result = result.substring(0,correct.length());
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test2");
		}
	}

	static public void testArray2(){
		total++;
		double[] correct = {123.4,56,98,174,215.8};
		String input = "123.4 56.0 98.0 174.0 215.8";
		getOutput(input);
		double[] result = student.userWeights;
		if (Arrays.equals(result, correct)){
			passed++;
		}
		else{
			failed.add("testArray2");
		}
	}

	public static void test3(){
		total++;
		String correct = "Enter weight 1:\nEnter weight 2:\nEnter weight 3:\nEnter weight 4:\nEnter weight 5:\n";
		correct += "You entered: 236.0 89.5 142.0 166.3 93.0 \n";
		correct += "\nTotal weight: 726.8\n";
		String result = getOutput("236.0 89.5 142.0 166.3 93.0");
		result = result.substring(0,correct.length());
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test3");
		}
	}

	public static void test4(){
		total++;
		String correct = "Enter weight 1:\nEnter weight 2:\nEnter weight 3:\nEnter weight 4:\nEnter weight 5:\n";
		correct += "You entered: 236.0 89.5 142.0 166.3 93.0 \n";
		correct += "\nTotal weight: 726.8\n";
		correct += "Average weight: 145.35999999999999\n";
		String result = getOutput("236.0 89.5 142.0 166.3 93.0");
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
		String correct = "Enter weight 1:\nEnter weight 2:\nEnter weight 3:\nEnter weight 4:\nEnter weight 5:\n";
		correct += "You entered: 236.0 89.5 142.0 166.3 93.0 \n";
		correct += "\nTotal weight: 726.8\n";
		correct += "Average weight: 145.35999999999999\n";
		correct += "Max weight: 236.0\n";
		String result = getOutput("236.0 89.5 142.0 166.3 93.0");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test5");
		}
	}

	public static void test6(){
		total++;
		String correct = "Enter weight 1:\nEnter weight 2:\nEnter weight 3:\nEnter weight 4:\nEnter weight 5:\n";
		correct += "You entered: 123.4 56.0 98.0 174.0 215.8 \n";
		correct += "\nTotal weight: 667.2\n";
		correct += "Average weight: 133.44\n";
		correct += "Max weight: 215.8\n";
		String result = getOutput("123.4 56.0 98.0 174.0 215.8");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test6");
		}
	}

	public static void hidden1(){
		total++;
		String correct = "Enter weight 1:\nEnter weight 2:\nEnter weight 3:\nEnter weight 4:\nEnter weight 5:\n";
		correct += "You entered: 1.2 3.5 6.7 8.9 0.0 \n";
		correct += "\nTotal weight: 20.3\n";
		correct += "Average weight: 4.0600000000000005\n";
		correct += "Max weight: 8.9\n";
		String result = getOutput("1.2 3.5 6.7 8.9 0.0");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("hidden1");
		}
	}

	public static void hidden2(){
		total++;
		String correct = "Enter weight 1:\nEnter weight 2:\nEnter weight 3:\nEnter weight 4:\nEnter weight 5:\n";
		correct += "You entered: 60.0 60.0 20.0 50.0 70.0 \n";
		correct += "\nTotal weight: 260.0\n";
		correct += "Average weight: 52.0\n";
		correct += "Max weight: 70.0\n";
		String result = getOutput("60 60 20 50 70");
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
