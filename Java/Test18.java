import java.io.*;

public class Test18 {
  static ParseStrings student = new ParseStrings();
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
    setInput("John, Simonsen\nq\n");
    student.main(args);
    String correct = "Enter input string:\n";
    String result = getOutput().substring(0,correct.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test2
    setOutput();
    total++;
    setInput("John Simonsen\nJohnSimonsen\nJohn  Simonsen\nq\n");
    student.main(args);
    correct = "Enter input string:\nError: No comma in string.\n\nEnter input string:\nError: No comma in string.\n\nEnter input string:\nError: No comma in string.\n\nEnter input string:\n";
    result = getOutput().substring(0,correct.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test3
    setOutput();
    total++;
    setInput("John, Simonsen\nq\n");
    student.main(args);
    correct = "Enter input string:\nFirst word: John\nSecond word: Simonsen\n";
    result = getOutput().substring(0,correct.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test4
    setOutput();
    total++;
    setInput("John, Simonsen\nLuke , Skywalker\nLayton,UT\nq\n");
    student.main(args);
    correct = "Enter input string:\nFirst word: John\nSecond word: Simonsen\n\n";
    correct += "Enter input string:\nFirst word: Luke\nSecond word: Skywalker\n\n";
    correct += "Enter input string:\nFirst word: Layton\nSecond word: UT\n\n";
    correct += "Enter input string:\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }

    //hidden test
    setOutput();
    total++;
    setInput("Leia , Organa\nDarth,Vader\nDeath, Star\nq\n");
    student.main(args);
    correct = "Enter input string:\nFirst word: Leia\nSecond word: Organa\n\n";
    correct += "Enter input string:\nFirst word: Darth\nSecond word: Vader\n\n";
    correct += "Enter input string:\nFirst word: Death\nSecond word: Star\n\n";
    correct += "Enter input string:\n";
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
