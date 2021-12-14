import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.util.ArrayList;
import java.io.File;
import java.io.PrintWriter;
import java.io.FileNotFoundException;
import java.util.Random;
import java.util.Arrays;

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
		System.out.printf("%d/%d\n",passed,total);
	}

	public static void test1(){
		total++;
		int[] correct = {0,1,0,0,1,1,1,3,1,1,2};
		int[] result = student.dice(11,new Random(0));
		if (Arrays.equals(result,correct){
			passed++;
		}
		else{
			failed.add("test1");
		}
	}

	public static void test2(){
		total++;
		int[] correct = {2,4,6,1,4,7,8,6,5,5,2};
		int[] result = student.dice(50,new Random(14));
		if (Arrays.equals(result,correct){
			passed++;
		}
		else{
			failed.add("test2");
		}
	}

	public static void test3(){
		total++;
		String correct = "Dice roll histogram:\n\n";
		String star = "****(4)\n";
		for(int i=2; i<13; i++){
			correct += i+":\t"+star;
		}
		int[] input = {4,4,4,4,4,4,4,4,4,4,4};
		String result = student.histogram(input);
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test3");
		}
	}

public static void test4(){
		total++;
		String correct = "Dice roll histogram:\n\n";
		correct += "2:\t**(2)\n"+"3:\t***(3)\n"+"4:\t*****(5)\n"+"5:\t***(3)\n";
		correct += "6:\t***(3)\n"+"7:\t***(3)\n"+"8:\t*****(5)\n"+"9:\t********(8)\n";
		correct += "10:\t****(4)\n"+"11:\t*(1)\n"+"12:\t***(3)\n";
		int[] input = {2,3,5,3,3,3,5,8,4,1,3};
		String result = student.histogram(input);
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test4");
		}
	}

	public static void test5(){
		total++;
		String correct = "Enter number of rolls:\nDice roll histogram:\n\n";
		correct += "2:\t**(2)\n3:\t****(4)\n4:\t******(6)\n5:\t*(1)\n6:\t****(4)\n";
		correct += "7:\t*******(7)\n8:\t********(8)\n9:\t******(6)\n10:\t*****(5)\n";
		correct += "11:\t*****(5)\n12:\t**(2)\n\n";
		String input = "50";
		String result = getOutput(input, 14);
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test5");
		}
	}

	public static void test6(){
		total++;
		String correct = "Enter number of rolls:\n";
		correct += "Invalid rolls. Try again.\n";
		String input = "0";
		String result = getOutput(input);
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test6");
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
		String[] args = {};
		student.main(args);
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
