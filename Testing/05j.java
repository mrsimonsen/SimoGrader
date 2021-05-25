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
		System.out.printf("%d/%d\n",passed,total);
	}

  public static String tests(){
    int total = 0;
    int score = 0;
    setOutput();
    //test1
    total++;
    setInput("IDK how that happened. TTYL.");
    student.main(args);
    String correct = "Enter text:\nYou entered: IDK how that happened. TTYL.\n";
    String result = getOutput().substring(0,correct.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test2
    setOutput();
    total++;
    setInput("IDK how that happened. TTYL.");
    student.main(args);
    correct = "Enter text:\nYou entered: IDK how that happened. TTYL.\n";
    correct += "\nReplaced \"IDK\" with \"I don't know\".\nReplaced \"TTYL\" with \"talk to you later\".\n";
    correct += "\nExpanded: I don't know how that happened. talk to you later.\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test3
    setOutput();
    total++;
    setInput("I'll fix it. JK, you know IDK how.");
    student.main(args);
    correct = "Enter text:\nYou entered: I'll fix it. JK, you know IDK how.\n";
    correct += "\nReplaced \"IDK\" with \"I don't know\".\nReplaced \"JK\" with \"just kidding\".\n";
    correct += "\nExpanded: I'll fix it. just kidding, you know I don't know how.\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test4
    setOutput();
    total++;
    setInput("Your bff, my BFF, and her BFF are all there.");
    student.main(args);
    correct = "Enter text:\nYou entered: Your bff, my BFF, and her BFF are all there.\n";
    correct += "\nReplaced \"BFF\" with \"best friend forever\".\n";
    correct += "\nExpanded: Your bff, my best friend forever, and her best friend forever are all there.\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }

    //hidden tests
    setOutput();
    total++;
    setInput("JK, IDK if TMI BFF. TTYL");
    student.main(args);
    correct = "Enter text:\nYou entered: JK, IDK if TMI BFF. TTYL\n";
    correct += "\nReplaced \"BFF\" with \"best friend forever\".\nReplaced \"IDK\" with \"I don't know\".\nReplaced \"JK\" with \"just kidding\".\nReplaced \"TMI\" with \"too much information\".\nReplaced \"TTYL\" with \"talk to you later\".\n";
	correct += "\nExpanded: just kidding, I don't know if too much information best friend forever. talk to you later\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }

    //testing complete
    String rep = ""+ score +"/"+total;
    return rep;
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
