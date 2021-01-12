import java.io.*;

public class Test04 {
  static TextMsgDecoder student = new TextMsgDecoder();
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
    setInput("IDK if I'll go. It's my BFF's birthday.");
    student.main(args);
    String correct = "Enter text:\nYou entered: IDK if I'll go. It's my BFF's birthday.\n";
    String result = getOutput().substring(0,correct.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test2
    setOutput();
    total++;
    setInput("Nice pic, TMI haha JK. TTYL");
    student.main(args);
    correct = "Enter text:\nYou entered: Nice pic, TMI haha JK. TTYL\n";
    result = getOutput().substring(0,correct.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test3
    setOutput();
    total++;
    setInput("IDK if I'll go. It's my BFF's birthday.");
    student.main(args);
    correct = "Enter text:\nYou entered: IDK if I'll go. It's my BFF's birthday.\n";
    correct += "BFF: best friend forever\nIDK: I don't know\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test4
    setOutput();
    total++;
    setInput("Nice pic, TMI haha JK. TTYL");
    student.main(args);
    correct = "Enter text:\nYou entered: Nice pic, TMI haha JK. TTYL\n";
    correct += "JK: just kidding\nTMI: too much information\nTTYL: talk to you later\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }

    //hidden tests
    total++;
    setOutput();
    setInput("JK, IDK if TMI BFF. TTYL");
    student.main(args);
    correct = "Enter text:\nYou entered: JK, IDK if TMI BFF. TTYL\n";
    correct += "BFF: best friend forever\nIDK: I don't know\nJK: just kidding\nTMI: too much information\nTTYL: talk to you later\n";
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
