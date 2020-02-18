import java.io.*;

public class Test01 {
  static BasicInput student = new BasicInput();
  private static ByteArrayOutputStream TOut;
  private static ByteArrayInputStream TIn;
  private static final PrintStream SOut = System.out;
  private static final InputStream SIn = System.in;
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
    setInput("10 2.2 a this ");
    student.main(args);
    String correct = "Enter integer:\nEnter double:\nEnter character:\nEnter string:\n10 2.2 a this\n";
    String out = getOutput();
    String result = out.substring(0,correct.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    setOutput();
    //test2
    total++;
    setInput("104 0.235 S stringy");
    student.main(args);
    correct = "Enter integer:\nEnter double:\nEnter character:\nEnter string:\n104 0.235 S stringy\n";
    correct += "stringy S 0.235 104\n";
    out = getOutput();
    result = out.substring(0,correct.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    setOutput();
    //test3
    total++;
    setInput("14 13.235 J cheese");
    student.main(args);
    correct = "Enter integer:\nEnter double:\nEnter character:\nEnter string:\n14 13.235 J cheese\n";
    correct += "cheese J 13.235 14\n";
	correct += "13.235 cast to an integer is 13\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    setOutput();

    //hidden tests
    total++;
    setInput("05 14.99 S Simonsen");
    student.main(args);
    correct = "Enter integer:\nEnter double:\nEnter character:\nEnter string:\n5 14.99 S Simonsen\n";
    correct += "Simonsen S 14.99 5\n";
    correct += "14.99 cast to an integer is 14\n";
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
  private static String getOutput(){
    return TOut.toString();
  }
  public static void restoreSystem(){
    System.setOut(SOut);
    System.setIn(SIn);
  }
}
