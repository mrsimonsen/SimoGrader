import java.io.*;

public class Test07 {
  static DrawHalfArrow student = new DrawHalfArrow();
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
    setInput("5 2 4");
    student.main(args);
    String correct = "Enter arrow base height:\nEnter arrow base width:\nEnter arrow head width:\n";
    correct += "\n**\n**\n**\n**\n**\n";
    String result = getOutput().substring(0,correct.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test2
    setOutput();
    total++;
    setInput("2 3 4");
    student.main(args);
    correct = "Enter arrow base height:\nEnter arrow base width:\nEnter arrow head width:\n";
    correct += "\n***\n***\n";
    result = getOutput().substring(0,correct.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test3
    setOutput();
    total++;
    setInput("3 3 7");
    student.main(args);
    correct = "Enter arrow base height:\nEnter arrow base width:\nEnter arrow head width:\n";
    correct += "\n***\n***\n***\n*******\n******\n*****\n****\n***\n**\n*\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test4
    setOutput();
    total++;
    setInput("5 1 3");
    student.main(args);
    correct = "Enter arrow base height:\nEnter arrow base width:\nEnter arrow head width:\n";
    correct += "\n*\n*\n*\n*\n*\n***\n**\n*\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test5
    setOutput();
    total++;
    setInput("2 4 3 4 8");
    student.main(args);
    correct = "Enter arrow base height:\nEnter arrow base width:\nEnter arrow head width:\nEnter arrow head width:\nEnter arrow head width:\n";
    correct += "\n****\n****\n********\n*******\n******\n*****\n****\n***\n**\n*\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }

    //hidden tests
    setOutput();
    total++;
    setInput("3 2 1 2 3");
    student.main(args);
    correct = "Enter arrow base height:\nEnter arrow base width:\nEnter arrow head width:\nEnter arrow head width:\nEnter arrow head width:\n";
    correct += "\n**\n**\n**\n***\n**\n*\n";
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
