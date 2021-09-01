import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.util.ArrayList;
import java.io.File;
import java.io.PrintWriter;
import java.io.FileNotFoundException;

// 09j
public class Tests {
	static PlayerRoster student = new PlayerRoster();
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
		hidden1();
		hidden2();
		hidden3();
		System.out.printf("%d/%d\n",passed,total);
	}

	public static void test1(){
		total++;
		String correct = "Enter player 1's jersey number:\nEnter player 1's rating:\n\nEnter player 2's jersey number:\nEnter player 2's rating:\n\nEnter player 3's jersey number:\nEnter player 3's rating:\n\nEnter player 4's jersey number:\nEnter player 4's rating:\n\nEnter player 5's jersey number:\nEnter player 5's rating:\n\n";
		correct += "ROSTER\nPlayer 1 -- Jersey number: 1, Rating: 4\nPlayer 2 -- Jersey number: 6, Rating: 9\nPlayer 3 -- Jersey number: 21, Rating: 5\nPlayer 4 -- Jersey number: 47, Rating: 8\nPlayer 5 -- Jersey number: 83, Rating: 2\n";
		String result = getOutput("1 4 6 9 21 5 47 8 83 2 q");
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
		String correct = "Enter player 1's jersey number:\nEnter player 1's rating:\n\nEnter player 2's jersey number:\nEnter player 2's rating:\n\nEnter player 3's jersey number:\nEnter player 3's rating:\n\nEnter player 4's jersey number:\nEnter player 4's rating:\n\nEnter player 5's jersey number:\nEnter player 5's rating:\n\n";
		correct += "ROSTER\nPlayer 1 -- Jersey number: 1, Rating: 4\nPlayer 2 -- Jersey number: 6, Rating: 9\nPlayer 3 -- Jersey number: 21, Rating: 5\nPlayer 4 -- Jersey number: 47, Rating: 8\nPlayer 5 -- Jersey number: 83, Rating: 2\n";
		String result = getOutput("1 4 6 9 21 5 47 8 83 2 q");
		result = result.substring(0,correct.length());
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test2");
		}
	}

	public static voicd test3(){
		total++;
		String correct = "Enter player 1's jersey number:\nEnter player 1's rating:\n\nEnter player 2's jersey number:\nEnter player 2's rating:\n\nEnter player 3's jersey number:\nEnter player 3's rating:\n\nEnter player 4's jersey number:\nEnter player 4's rating:\n\nEnter player 5's jersey number:\nEnter player 5's rating:\n";
		correct += "\nROSTER\nPlayer 1 -- Jersey number: 84, Rating: 7\nPlayer 2 -- Jersey number: 23, Rating: 4\nPlayer 3 -- Jersey number: 4, Rating: 5\nPlayer 4 -- Jersey number: 30, Rating: 2\nPlayer 5 -- Jersey number: 66, Rating: 9\n";
		String result = getOutput("84 7 23 4 4 5 30 2 66 9 q");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test3()");
		}
	}

	public static void test4(){
		total++;
		String correct = "Enter player 1's jersey number:\nEnter player 1's rating:\n\nEnter player 2's jersey number:\nEnter player 2's rating:\n\nEnter player 3's jersey number:\nEnter player 3's rating:\n\nEnter player 4's jersey number:\nEnter player 4's rating:\n\nEnter player 5's jersey number:\nEnter player 5's rating:\n";
		correct += "\nROSTER\nPlayer 1 -- Jersey number: 84, Rating: 7\nPlayer 2 -- Jersey number: 23, Rating: 4\nPlayer 3 -- Jersey number: 4, Rating: 5\nPlayer 4 -- Jersey number: 30, Rating: 2\nPlayer 5 -- Jersey number: 66, Rating: 9\n";
		correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
		correct += "ROSTER\nPlayer 1 -- Jersey number: 84, Rating: 7\nPlayer 2 -- Jersey number: 23, Rating: 4\nPlayer 3 -- Jersey number: 4, Rating: 5\nPlayer 4 -- Jersey number: 30, Rating: 2\nPlayer 5 -- Jersey number: 66, Rating: 9\n";
		correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
		String result = getOutput("84 7 23 4 4 5 30 2 66 9 o q");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test4");
		}
	}

	public static void test5(){
		total++;
		String correct = "Enter player 1's jersey number:\nEnter player 1's rating:\n\nEnter player 2's jersey number:\nEnter player 2's rating:\n\nEnter player 3's jersey number:\nEnter player 3's rating:\n\nEnter player 4's jersey number:\nEnter player 4's rating:\n\nEnter player 5's jersey number:\nEnter player 5's rating:\n";
		correct += "\nROSTER\nPlayer 1 -- Jersey number: 84, Rating: 7\nPlayer 2 -- Jersey number: 23, Rating: 4\nPlayer 3 -- Jersey number: 4, Rating: 5\nPlayer 4 -- Jersey number: 30, Rating: 2\nPlayer 5 -- Jersey number: 66, Rating: 9\n";
		correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
		correct += "Enter a jersey number:\nEnter a new rating for player:\n";
		correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
		correct += "ROSTER\nPlayer 1 -- Jersey number: 84, Rating: 7\nPlayer 2 -- Jersey number: 23, Rating: 4\nPlayer 3 -- Jersey number: 4, Rating: 6\nPlayer 4 -- Jersey number: 30, Rating: 2\nPlayer 5 -- Jersey number: 66, Rating: 9\n";
		correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
		String result = getOutput("84 7 23 4 4 5 30 2 66 9 u 4 6 o q");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test5");
		}
	}

	public static void test6(){
		total++;
		String correct = "Enter player 1's jersey number:\nEnter player 1's rating:\n\nEnter player 2's jersey number:\nEnter player 2's rating:\n\nEnter player 3's jersey number:\nEnter player 3's rating:\n\nEnter player 4's jersey number:\nEnter player 4's rating:\n\nEnter player 5's jersey number:\nEnter player 5's rating:\n";
		correct += "\nROSTER\nPlayer 1 -- Jersey number: 84, Rating: 7\nPlayer 2 -- Jersey number: 23, Rating: 4\nPlayer 3 -- Jersey number: 4, Rating: 5\nPlayer 4 -- Jersey number: 30, Rating: 2\nPlayer 5 -- Jersey number: 66, Rating: 9\n";
		correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
		correct += "Enter a rating:\n\nABOVE 4\nPlayer 1 -- Jersey number: 84, Rating: 7\nPlayer 3 -- Jersey number: 4, Rating: 5\nPlayer 5 -- Jersey number: 66, Rating: 9\n";
		correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
		String result = getOutput("84 7 23 4 4 5 30 2 66 9 a 4 q");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test6");
		}
	}

	public static void test7(){
		total++;
		String correct = "Enter a rating:\n\nABOVE 5\nPlayer 1 -- Jersey number: 12, Rating: 7\nPlayer 5 -- Jersey number: 90, Rating: 6\n";
		correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
		String result = getOutput("12 7 47 2 33 2 19 5 90 6 a 5 q");
		result = result.substring(result.length()-correct.length(),result.length());
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test7");
		}
	}

	public static void test8(){
		total++;
		String correct = "Enter player 1's jersey number:\nEnter player 1's rating:\n\nEnter player 2's jersey number:\nEnter player 2's rating:\n\nEnter player 3's jersey number:\nEnter player 3's rating:\n\nEnter player 4's jersey number:\nEnter player 4's rating:\n\nEnter player 5's jersey number:\nEnter player 5's rating:\n";
		correct += "\nROSTER\nPlayer 1 -- Jersey number: 84, Rating: 7\nPlayer 2 -- Jersey number: 23, Rating: 4\nPlayer 3 -- Jersey number: 4, Rating: 5\nPlayer 4 -- Jersey number: 30, Rating: 2\nPlayer 5 -- Jersey number: 66, Rating: 9\n";
		correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
		correct += "Enter a jersey number:\nEnter a new jersey number:\nEnter a rating for the new player:\n";
		correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
		correct += "ROSTER\nPlayer 1 -- Jersey number: 84, Rating: 7\nPlayer 2 -- Jersey number: 23, Rating: 4\nPlayer 3 -- Jersey number: 4, Rating: 5\nPlayer 4 -- Jersey number: 30, Rating: 2\nPlayer 5 -- Jersey number: 15, Rating: 6\n";
		correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
		String result = getOutput("84 7 23 4 4 5 30 2 66 9 r 66 15 6 o q");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test8");
		}
	}

	public static void test9(){
		total++;
		String correct = "Enter player 1's jersey number:\nEnter player 1's rating:\n\nEnter player 2's jersey number:\nEnter player 2's rating:\n\nEnter player 3's jersey number:\nEnter player 3's rating:\n\nEnter player 4's jersey number:\nEnter player 4's rating:\n\nEnter player 5's jersey number:\nEnter player 5's rating:\n";
		correct += "\nROSTER\nPlayer 1 -- Jersey number: 84, Rating: 7\nPlayer 2 -- Jersey number: 23, Rating: 4\nPlayer 3 -- Jersey number: 4, Rating: 5\nPlayer 4 -- Jersey number: 30, Rating: 2\nPlayer 5 -- Jersey number: 66, Rating: 9\n";
		correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
		correct += "Enter a jersey number:\n";
		correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
		correct += "ROSTER\nPlayer 1 -- Jersey number: 84, Rating: 7\nPlayer 2 -- Jersey number: 23, Rating: 4\nPlayer 3 -- Jersey number: 4, Rating: 5\nPlayer 4 -- Jersey number: 30, Rating: 2\nPlayer 5 -- Jersey number: 66, Rating: 9\n";
		correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
		String result = getOutput("84 7 23 4 4 5 30 2 66 9 r 12 o q");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test9");
		}
	}

	public static void hidden1(){
		total++;
		String correct = "Enter player 1's jersey number:\nEnter player 1's rating:\n\nEnter player 2's jersey number:\nEnter player 2's rating:\n\nEnter player 3's jersey number:\nEnter player 3's rating:\n\nEnter player 4's jersey number:\nEnter player 4's rating:\n\nEnter player 5's jersey number:\nEnter player 5's rating:\n";
		correct += "\nROSTER\nPlayer 1 -- Jersey number: 1, Rating: 1\nPlayer 2 -- Jersey number: 2, Rating: 2\nPlayer 3 -- Jersey number: 3, Rating: 3\nPlayer 4 -- Jersey number: 4, Rating: 4\nPlayer 5 -- Jersey number: 5, Rating: 5\n";
		correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
		correct += "Enter a jersey number:\nEnter a new jersey number:\nEnter a rating for the new player:\n";
		correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
		correct += "ROSTER\nPlayer 1 -- Jersey number: 1, Rating: 1\nPlayer 2 -- Jersey number: 2, Rating: 2\nPlayer 3 -- Jersey number: 3, Rating: 3\nPlayer 4 -- Jersey number: 4, Rating: 4\nPlayer 5 -- Jersey number: 6, Rating: 6\n";
		correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
		String result = getOutput("1 1 2 2 3 3 4 4 5 5 r 5 6 6 o q");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("hidden1");
		}
	}

	public static void hidden2(){
		total++;
		String correct = "Enter player 1's jersey number:\nEnter player 1's rating:\n\nEnter player 2's jersey number:\nEnter player 2's rating:\n\nEnter player 3's jersey number:\nEnter player 3's rating:\n\nEnter player 4's jersey number:\nEnter player 4's rating:\n\nEnter player 5's jersey number:\nEnter player 5's rating:\n";
		correct += "\nROSTER\nPlayer 1 -- Jersey number: 84, Rating: 7\nPlayer 2 -- Jersey number: 23, Rating: 4\nPlayer 3 -- Jersey number: 4, Rating: 5\nPlayer 4 -- Jersey number: 30, Rating: 2\nPlayer 5 -- Jersey number: 66, Rating: 9\n";
		correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
		correct += "Enter a jersey number:\nEnter a new rating for player:\n";
		correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
		correct += "ROSTER\nPlayer 1 -- Jersey number: 84, Rating: 7\nPlayer 2 -- Jersey number: 23, Rating: 4\nPlayer 3 -- Jersey number: 4, Rating: 8\nPlayer 4 -- Jersey number: 30, Rating: 2\nPlayer 5 -- Jersey number: 66, Rating: 9\n";
		correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
		String result = getOutput("84 7 23 4 4 5 30 2 66 9 u 4 8 o q");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("hidden2");
		}
	}

	public static void hidden3(){
		total++;
		String correct = "Enter player 1's jersey number:\nEnter player 1's rating:\n\nEnter player 2's jersey number:\nEnter player 2's rating:\n\nEnter player 3's jersey number:\nEnter player 3's rating:\n\nEnter player 4's jersey number:\nEnter player 4's rating:\n\nEnter player 5's jersey number:\nEnter player 5's rating:\n";
		correct += "\nROSTER\nPlayer 1 -- Jersey number: 84, Rating: 7\nPlayer 2 -- Jersey number: 23, Rating: 4\nPlayer 3 -- Jersey number: 4, Rating: 5\nPlayer 4 -- Jersey number: 30, Rating: 2\nPlayer 5 -- Jersey number: 66, Rating: 9\n";
		correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
		correct += "Enter a rating:\n\nABOVE 7\nPlayer 5 -- Jersey number: 66, Rating: 9\n";
		correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
		String result = getOutput("84 7 23 4 4 5 30 2 66 9 a 7 q");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("hidden3");
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
