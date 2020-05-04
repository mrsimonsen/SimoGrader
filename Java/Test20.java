import java.util.Arrays;
import java.util.Scanner;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.io.InputStream;
import java.io.File;
import java.io.FileNotFoundException;

public class Test20 {
  static CaesarCipher student = new CaesarCipher();
  static private ByteArrayOutputStream TOut;
  static private ByteArrayInputStream TIn;
  static private final PrintStream SOut = System.out;
  static private final InputStream SIn = System.in;

  public static void main(String[] args){
	  System.out.println(tests());    
  }

  public static String tests(){
    int total = 0;
    int score = 0;
    //test1
    total++;
    String message = "Holy letters Batman, this is a string.";
    int[] r = Support.letterDistr(message);
    int[] c = {3,1,0,0,2,0,1,2,3,0,0,2,1,2,1,0,0,2,4,5,0,0,0,0,1,0};
    if (Arrays.equals(r,c)){
      score++;
    }
    //test2
    total++;
    message = "This is my message.";
    String result = Support.encrypt(message, 14);
    String correct = "Hvwg wg am asggous.";
    if (result.equals(correct)){
      score++;
    }
    //test3
    total++;
    message = "Hvwg wg am asggous.";
    result = Support.decrypt(message, 14);
    correct = "This is my message.";
    if (result.equals(correct)){
      score++;
    }
    //test4
    total++;
    Scanner sinput = null;
    String fname = "secret.txt";
	String rout = "result";
	String cout = "correct";
	 try{
		sinput = ReadWrite.open_file(fname,sinput);
    	File file =	new File(fname);
    	Scanner cinput	= new	Scanner(file);	 
		rout = sinput.nextLine();
    	cout = cinput.nextLine();
	 }
	  catch (FileNotFoundException e){
		  System.out.println(e);
	  }


    if (rout.equals(cout)){
      score++;
    }

    //hidden test
    total++;
    setOutput();
    String[] args = {};
    student.main(args);
    setInput("4\ntest.txt\nn\n5\ny\ntext.txt\nn\n0\n");
    correct = "a:   2|**\nb:   1|*\nc:   0|\nd:   2|**\ne:   5|*****\nf:   2|**\ng:   1|*\nh:   1|*\ni:   2|**\nj:   0|\nk:   0|\nl:   2|**\nm:   0|\nn:   0|\no:   6|******\np:   0|\nq:   0|\nr:   3|***\ns:   1|*\nt:   2|**\nu:   2|**\nv:   0|\nw:   1|*\nx:   0|\ny:   2|**\nz:   0|\nWould you like to see the menu again?: \nWhat is your choice?: \nThank you for using the utility and goodbye~\n";
    result = getOutput();
    //result = result.substring(result.length()-correct.length(),result.length());
    restoreSystem();
	  System.out.println("hello");
    if (result.equals(correct)){
      score++;
    }

    //testing complete
    String rep = ""+ score +"/"+total;
    return rep;
  }

  //Set up methods
  static public void setOutput(){
    TOut = new ByteArrayOutputStream();
    System.setOut(new PrintStream(TOut));
  }
  private static void setInput(String data){
  TIn = new ByteArrayInputStream(data.getBytes());
  System.setIn(TIn);
  }
  static private String getOutput(){
    return TOut.toString();
  }
  static public void restoreSystem(){
    System.setOut(SOut);
    System.setIn(SIn);
  }
}
