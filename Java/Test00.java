import java.io.*;

public class Test00 {
  static HelloWorld student = new HelloWorld();
  private static ByteArrayOutputStream TOut;
  private static ByteArrayInputStream TIn;
  private static final PrintStream SOut = System.out;
  private static final InputStream SIn = System.in;
  public static String[] args;

  public static void main(String[] args){
    System.out.println(tests());
  }

  public static String tests(){
    int total = 0;
    int score = 0;
    setOutput();
    //test1
    total++;
    student.main(args);
    //need to add '/r' for windows when grading, stupid windows
    String correct = "Hello World!\n";
    String result = getOutput();
    if (result.equals(correct)){
      score++;
    }
    //no hidden tests for assignment 00
    //testing complete
    restoreSystem();
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
  private static String getOutput(){
    return TOut.toString();
  }
  public static void restoreSystem(){
    System.setOut(SOut);
    System.setIn(SIn);
  }
}
