import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.util.ArrayList;
import java.io.File;
import java.io.PrintWriter;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Random;
import java.util.Arrays;

// 21j
public class Tests {
	static Yahtzee student = new Yahtzee();
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
		int correct = 4;
		String input = "30 4";
		int result = student.holding(new Scanner(input));
		if (result == correct){
			score++;
		}
		else{
			failed.add("test1");
		}
	}

	public static void test2(){
		total++;
		int correct = 0;
		String input = "0";
		int result = student.holding(new Scanner(input));
		if (result == correct){
			score++;
		}
		else{
			failed.add("test2");
		}
	}

	public static void test3(){
		total++;
		int[] correct = {1,2,3,4,5};
		String input = " 14 1 ";
		int[] start = {1,2,3,4,5};
		int[] result = student.rerollDice(start,new Scanner(input),new Random(0),4);
		if (Arrays.equals(result, correct)){
			score++;
		}
		else{
			failed.add("test3");
		}
	}

	public static void test4(){
		total++;
		int[] correct = {6,2,1,4,6};
		String input = " 14 1 3 5 ";
		int[] start = {1,2,3,4,5};
		int[] result = student.rerollDice(start,new Scanner(input),new Random(25),2);
		if (Arrays.equals(result, correct)){
			score++;
		}
		else{
			failed.add("test4");
		}
	}

	public static void test5(){
		total++;
		String correct = "1 2 3 4 5";
		String correctSpace = "1 2 3 4 5 ";
		int[] dice  = {1,2,3,4,5};
		String result = student.printDice(dice);
		if (result.equals(correct)||result.equals(correctSpace)){
			score++;
		}
		else{
			failed.add("test5");
		}
	}

	public static void test6(){
		total++;
		String correct = "5 4 3 2 1";
		String correctSpace = "5 4 3 2 1 ";
		int[] dice = {5,4,3,2,1};
		String result = student.printDice(dice);
		if (result.equals(correct)||result.equals(correctSpace)){
			score++;
		}
		else{
			failed.add("test6");
		}
	}

	public static void test7(){
		total++;
		int[] correct = {2,0,1,0,1,1};
		int[] dice = {1,1,3,5,6};
		int[] result = student.kinds(dice);
		if (Arrays.equals(result, correct)){
			score++;
		}
		else{
			failed.add("test7");
		}
	}

	public static void test8(){
		total++;
		int[] correct = {0,1,1,2,0,1};
		int[] dice = {2,3,4,4,6};
		int[] result = student.kinds(dice);
		if (Arrays.equals(result, correct)){
			score++;
		}
		else{
			failed.add("test8");
		}
	}

	public static void test9(){
		total++;
		String correct = "Yahtzee";
		//6 possible Yahtzees
		int[][] dice = {{4,4,4,4,4},{6,6,6,6,6},{5,5,5,5,5},{3,3,3,3,3},{2,2,2,2,2},{1,1,1,1,1}};
		String[] correctArray = new String[6];
		for (int i = 0; i<6; i++){
			correctArray[i] = correct;
		}
		String[] resultArray = new String[6];
		for (int i = 0; i < 6; i++){
			resultArray[i] = student.printScore(dice[i]);
		}
		if (Arrays.equals(correctArray,resultArray)){
			score++;
		}
		else{
			failed.add("test9");
		}
	}

	public static void test10(){
		total++;
		String correct = "Large Straight";
		//2 possible Large Straights
		int[][] dice = {{4,5,6,3,2},{5,2,4,1,3}};
		String[] correctArray = new String[2];
		for (int i = 0; i < 2; i++){
			correctArray[i] = correct;
		}
		String[] resultArray = new String[2];
		for (int i = 0; i < 2; i++){
			resultArray[i] = student.printScore(dice[i]);
		}
		if (Arrays.equals(correctArray, resultArray)){
			score++;
		}
		else{
			failed.add("test10");
		}
	}

	public static void test11(){
		total++;
		String correct = "Small Straight";
		//14 possible Small Straights
		int[][] dice = {
		{1,2,3,4,6},{1,2,3,4,1},{1,2,3,4,2},{1,2,3,4,3},{1,2,3,4,4},
		{2,3,4,5,2},{2,3,4,5,3},{2,3,4,5,4},{2,3,4,5,5},
		{3,4,5,6,6},{3,4,5,6,1},{3,4,5,6,3},{3,4,5,6,4},{3,4,5,6,5}
		};
		String[] correct Array = new String[14];
		for (int i = 0; i < 14; i++){
			correctArray[i] = correct;
		}
		String[] resultArray = new String[14];
		for (int i = 0; i < 14; i++){
			resultArray[i] = student.printScore(dice[i]);
		}
		if (Arrays.equals(correctArray,resultArray)){
			score++;
		}
		else{
			failed.add("test11");
		}
	}

	public static void test12(){
		total++;
		String correct = "Four of a Kind";
		//testing 2 of the possible 4 o' Kinds
		int[][] dice = {{4,4,3,4,4},{3,3,3,5,3}};
		String[] correctArray = new String[2];
		for (int i = 0; i < 2; i++){
			correctArray[i] = correct;
		}
		String[] resultArray = new String[2];
		for (int i = 0; i < 2; i++){
			resultArray[i] = student.printScore(dice[i]);
		}
		if (Arrays.equals(correctArray,resultArray)){
			score++;
		}

	public static void test13(){
		total++;
		String correct = "Full House";
		//testing 3 of the possible full houses
		int[][] dice = {{2,2,3,3,3},{4,4,4,6,6},{1,4,1,4,1}};
		String[] correctArray = new String[3];
		for (int i = 0; i < 3; i++){
			correctArray[i] = correct;
		}
		String[] resultArray = new String[3];
		for (int i = 0; i < 3; i++){
			resultArray[i] = student.printScore(dice[i]);
		}
		if (Arrays.equals(correctArray,resultArray)){
			score++;
		}
		else{	
			failed.add("test13");
		}
	}

	public static void test14(){
		total++;
		String correct = "Three of a Kind";
		//testing 2 of the possible 3 o' kinds
		int[][] dice = {{4,4,4,1,2},{1,3,5,3,3}};
		String[] correctArray = new String[2];
		for (int i = 0; i < 2; i++){
			correctArary[i] = correct;
		}
		String[] resultArray = new String[2];
		for (int i = 0; i < 2; i++){
			resultArray[i] = student.printScore(dice[i]);
		}
		if (Arrays.equals(correctArray,resultArray)){
			score++;
		}
		else{
			failed.add("test14");
		}
	}

	public static void test15(){
		total++;
		String correct = "You did not score anything noteworthy.";
		//testing 2 of the possible no score
		int[][] dice = {{1,1,4,5,3},{6,5,3,5,6}};
		String[] correctArray = new String[2];
		for (int i = 0; i < 2; i++){
			correctArray[i] = correct;
		}
		String[] resultArray = new String[2];
		for (int i = 0; i < 2; i++){
			resultArray[i] = student.printScore(dice[i]);
		}
		if (Arrays.equals(correctArray,resultArray)){
			score++;
		}
		else{
			failed.add("test15");
		}
	}
	//no hidden tests

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
