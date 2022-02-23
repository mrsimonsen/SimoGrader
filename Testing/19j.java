import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.util.ArrayList;
import java.io.File;
import java.io.PrintWriter;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;

// 20j
public class Tests {
	static CaesarCipher student = new CaesarCipher();
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
		System.out.printf("%d/%d\n",passed,total);
	}

	public static void test1(){
		total++;
		int[] result = Support.letterDistr("Holy letters Batman, this is a string.");
		int[] correct = {3,1,0,0,2,0,1,2,3,0,0,2,1,2,1,0,0,2,4,5,0,0,0,0,1,0};
		if (Arrays.equals(result,correct)){
			passed++;
		}
		else{
			failed.add("test1");
		}
	}

	public static void test2(){
		total++;
		String result = Support.encrypt("This is my message.", 14);
		String correct = "Hvwg wg am asggous.";
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test2");
		}
	}

	public static void test3(){
		total++;
		String result = Support.decrypt("Hvwg wg am asggous.", 14);
		String correct = "This is my message.";
		if (result.equals(correct)){
			passed++;
		}
		else{
			failed.add("test3");
		}
	}

	public static void test4(){
		total++;
		Scanner sinput = null;
		String fname = "secret.txt";
		String rout = "result";
		String cout = "correct";
		try{
			sinput = ReadWrite.openFile(fname,sinput);
			Scanner cinput = new Scanner(new File(fname));
			rout = sinput.nextLine();
			cout = cinput.nextLine();
			sinput.close();
			cinput.close();
		}
		catch (FileNotFoundException e){
			System.out.println(e);
		}
		if (rout.equals(cout)){
			passed++;
		}
		else{
			failed.add("test4");
		}
	}
/*
    //hidden test
    total++;
    setOutput();
    String[] args = {};
    student.main(args);
    setInput("4\ntest.txt\n2n\n5\ny\ntext.txt\nn\n0\n");//this sequence does not work.
    correct = "a:   2|**\nb:   1|*\nc:   0|\nd:   2|**\ne:   5|*****\nf:   2|**\ng:   1|*\nh:   1|*\ni:   2|**\nj:   0|\nk:   0|\nl:   2|**\nm:   0|\nn:   0|\no:   6|******\np:   0|\nq:   0|\nr:   3|***\ns:   1|*\nt:   2|**\nu:   2|**\nv:   0|\nw:   1|*\nx:   0|\ny:   2|**\nz:   0|\nWould you like to see the menu again?: \nWhat is your choice?: \nThank you for using the utility and goodbye~\n";
    result = getOutput();
    result = result.substring(result.length()-correct.length(),result.length());
    restoreSystem();
    if (result.equals(correct)){
      passed++;
    }
*/

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
