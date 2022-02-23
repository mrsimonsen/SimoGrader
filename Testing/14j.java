import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.util.ArrayList;
import java.io.File;
import java.io.PrintWriter;
import java.io.FileNotFoundException;
import java.util.Scanner;

// 14j
public class Tests {
	static AuthoringAssistant student = new AuthoringAssistant();
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
		test2a();
		test2b();
		test3();
		test4();
		test5();
		test6();
		test7();
		test8();
		hidden1();
		hidden2();
		System.out.printf("%d/%d\n",passed,total);
	}

	public static void test1(){
		total++;
		String correct = "Enter a sample text:\n\nYou entered: Testing that enterd text is repeated.\n";
		String result = getOutput("Testing that enterd text is repeated.\nq\n");
		result = result.substring(0,correct.length());
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test1");
		}
	}

	public static void test2a(){
		total++;
		String correct = "Enter a sample text:\n\nYou entered: Testing that menu is called and can quit.\n";
		correct += "\nMENU\nc - Number of non-whitespace characters\nw - Number of words\nf - Find text\nr - Replace all !\'s\ns - Shorten spaces\nq - Quit\n\nChoose an option:\n";
		String result = getOutput("Testing that menu is called and can quit.\nq\n");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test2a");
		}
	}

	public static void test2b(){
		total++;
		char correct = 'q';
		setOutput();
		char result = student.printMenu(new Scanner("1\nq\n"));
		restoreSystem();
		if (result == correct){
			passed++;
		}
		else{
			failed.add("test2b");
		}
	}

	public static void test3(){
		total++;
		int correct = 12;
		int result = student.getNumOfNonWSCharacters("This is a   test.");
		if (result == correct){
			passed++;
		}
		else{
			failed.add("test3");
		}
	}

	public static void test4(){
		total++;
		int correct = 4;
		int result = student.getNumOfWords("This is a   test.");
		if (result == correct){
			passed++;
		}
		else{
			failed.add("test4");
		}
	}

	public static void test5(){
		total++;
		int correct = 3;
		int result = student.findText("some water", "I want some water. I had some water earlier, but now he has some water.");
		if (result == correct){
			passed++;
		}
		else{
			failed.add("test5");
		}
	}

	public static void test6(){
		total++;
		String correct = "May the Force be with  you.";
		String result = student.replaceExclamation("May the Force be with  you!");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test6");
		}
	}

	public static void test7(){
		total++;
		String correct = "There are too many spaces here. Why?";
		String result = student.shortenSpace("             There are  too  many    spaces     here.      Why?");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test7");
		}
	}

	public static void test8(){
		total++;
		String correct = "Enter a sample text:\n\nYou entered: We'll continue our quest in space.  There will be more shuttle flights and more shuttle crews and,  yes,  more volunteers, more civilians,  more teachers in space.  Nothing ends here;  our hopes and our journeys continue!\n";
		correct += "\nMENU\nc - Number of non-whitespace characters\nw - Number of words\nf - Find text\nr - Replace all !\'s\ns - Shorten spaces\nq - Quit\n\nChoose an option:\n";
		correct += "Number of non-whitespace characters: 181\n";
		correct += "\nMENU\nc - Number of non-whitespace characters\nw - Number of words\nf - Find text\nr - Replace all !\'s\ns - Shorten spaces\nq - Quit\n\nChoose an option:\n";
		correct += "Number of words: 35\n";
		correct += "\nMENU\nc - Number of non-whitespace characters\nw - Number of words\nf - Find text\nr - Replace all !\'s\ns - Shorten spaces\nq - Quit\n\nChoose an option:\n";
		correct += "Enter a word or phrase to be found:\n\"more\" instances: 5\n";
		correct += "\nMENU\nc - Number of non-whitespace characters\nw - Number of words\nf - Find text\nr - Replace all !\'s\ns - Shorten spaces\nq - Quit\n\nChoose an option:\n";
		correct += "Edited text: We'll continue our quest in space.  There will be more shuttle flights and more shuttle crews and,  yes,  more volunteers, more civilians,  more teachers in space.  Nothing ends here;  our hopes and our journeys continue.\n";
		correct += "\nMENU\nc - Number of non-whitespace characters\nw - Number of words\nf - Find text\nr - Replace all !\'s\ns - Shorten spaces\nq - Quit\n\nChoose an option:\n";
		correct += "Edited text: We'll continue our quest in space. There will be more shuttle flights and more shuttle crews and, yes, more volunteers, more civilians, more teachers in space. Nothing ends here; our hopes and our journeys continue.\n";
		correct += "\nMENU\nc - Number of non-whitespace characters\nw - Number of words\nf - Find text\nr - Replace all !\'s\ns - Shorten spaces\nq - Quit\n\nChoose an option:\n";
		String result = getOutput("We'll continue our quest in space.  There will be more shuttle flights and more shuttle crews and,  yes,  more volunteers, more civilians,  more teachers in space.  Nothing ends here;  our hopes and our journeys continue!\nc\nw\nf\nmore\nr\ns\nq\n");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test8");
		}
	}

	public static void hidden1(){
		total++;
		String correct = "Enter a sample text:\n\nYou entered: I have a test! I am not prepared!\n";
		correct += "\nMENU\nc - Number of non-whitespace characters\nw - Number of words\nf - Find text\nr - Replace all !\'s\ns - Shorten spaces\nq - Quit\n\nChoose an option:\n";
		correct += "Edited text: I have a test. I am not prepared.\n";
		correct += "\nMENU\nc - Number of non-whitespace characters\nw - Number of words\nf - Find text\nr - Replace all !\'s\ns - Shorten spaces\nq - Quit\n\nChoose an option:\n";
		correct += "Number of words: 8\n";
		correct += "\nMENU\nc - Number of non-whitespace characters\nw - Number of words\nf - Find text\nr - Replace all !\'s\ns - Shorten spaces\nq - Quit\n\nChoose an option:\n";
		correct += "Number of non-whitespace characters: 26\n";
		correct += "\nMENU\nc - Number of non-whitespace characters\nw - Number of words\nf - Find text\nr - Replace all !\'s\ns - Shorten spaces\nq - Quit\n\nChoose an option:\n";
		String result = getOutput("I have a test! I am not prepared!\nr\nw\nc\nq\n");
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("hidden1");
		}
	}

	public static void hidden2(){
		total++;
		String correct = "";
		correct = "Enter a sample text:\n\nYou entered: I want some water. I had some water earlier, but now he has some water   .\n";
		correct += "\nMENU\nc - Number of non-whitespace characters\nw - Number of words\nf - Find text\nr - Replace all !\'s\ns - Shorten spaces\nq - Quit\n\nChoose an option:\n";
		correct += "Enter a word or phrase to be found:\n\"some water\" instances: 3\n";
		correct += "\nMENU\nc - Number of non-whitespace characters\nw - Number of words\nf - Find text\nr - Replace all !\'s\ns - Shorten spaces\nq - Quit\n\nChoose an option:\n";
		correct += "Edited text: I want some water. I had some water earlier, but now he has some water .\n";
		correct += "\nMENU\nc - Number of non-whitespace characters\nw - Number of words\nf - Find text\nr - Replace all !\'s\ns - Shorten spaces\nq - Quit\n\nChoose an option:\n";
		String result = getOutput("I want some water. I had some water earlier, but now he has some water   .\nf\nsome water\ns\nq\n");
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
