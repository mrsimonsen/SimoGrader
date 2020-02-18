import java.io.*;

public class Test05 {
  static TextMsgExpander student = new TextMsgExpander();
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
