import java.io.*;

public class Test13 {
  static TextAnalyzer student = new TextAnalyzer();
  static private ByteArrayOutputStream TOut;
  static private ByteArrayInputStream TIn;
  static private final PrintStream SOut = System.out;
  static private final InputStream SIn = System.in;
  static String[] args = {};

  public static void main(String[] args){
    System.out.println(tests());
  }

  public static String tests(){
    int total = 0;
    int score = 0;
    setOutput();
    //test1
    total++;
    setInput("The only thing we have to fear is fear itself.\n");
    student.main(args);
    String correct = "Enter a sentence or phrase:\n\nYou entered: The only thing we have to fear is fear itself.\n";
    String result = getOutput().substring(0,correct.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test2
    total++;
    int r = student.getNumOfCharacters("The only thing we have to fear is fear itself.");
    if (r==46){
      score++;
    }
    //test2
    total++;
    r = student.getNumOfCharacters("The rain in Spain stays mainly in the plain.");
    if (r == 44){
      score++;
    }
    //test3
    setOutput();
    total++;
    setInput("The only thing we have to fear is fear itself.\n");
    student.main(args);
    correct = "Enter a sentence or phrase:\n\nYou entered: The only thing we have to fear is fear itself.\n";
    correct += "\nNumber of characters: 46\n";
    result = getOutput().substring(0,correct.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test4
    setOutput();
    total++;
    setInput("The only thing we have to fear is fear itself.\n");
    student.main(args);
    correct = "Enter a sentence or phrase:\n\nYou entered: The only thing we have to fear is fear itself.\n";
    correct += "\nNumber of characters: 46\n";
    correct += "String with no whitespace: Theonlythingwehavetofearisfearitself.\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test5
    setOutput();
    total++;
    setInput("The rain in Spain stays mainly in the plain.\n");
    student.main(args);
    correct = "Enter a sentence or phrase:\n\nYou entered: The rain in Spain stays mainly in the plain.\n";
    correct += "\nNumber of characters: 44\n";
    correct += "String with no whitespace: TheraininSpainstaysmainlyintheplain.\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }

    //hidden tests
    setOutput();
    total++;
    setInput("May the Force be with you!\n");
    student.main(args);
    correct = "Enter a sentence or phrase:\n\nYou entered: May the Force be with you!\n";
    correct += "\nNumber of characters: 26\n";
    correct += "String with no whitespace: MaytheForcebewithyou!\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }

    total++;
    setOutput();
    setInput("Simonsen\n");
    student.main(args);
    correct = "Enter a sentence or phrase:\n\nYou entered: Simonsen\n";
    correct += "\nNumber of characters: 8\n";
    correct += "String with no whitespace: Simonsen\n";
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
  public static void toFile(String correct, String result){
	try{
		File c = new File("correct.txt");
		File r = new File("result.txt");
		PrintWriter wc = new PrintWriter(c);
		wc.print(correct);
		wc.close();
		PrintWriter wr = new PrintWriter(r);
		wr.print(result);
		wr.close();
	}
	catch (FileNotFoundException e){
		System.out.println("Couldn't create files.");
		System.out.println(e);
	}
  }
}
