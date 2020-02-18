import java.io.*;

public class Test06 {
  static DrawRightTriangle student = new DrawRightTriangle();
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
    setInput("@ 3");
    student.main(args);
    String correct = "Enter a character:\nEnter triangle height:\n";
    correct += "\n@ \n@ @ \n@ @ @ \n";
    String result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test2
    setOutput();
    total++;
    setInput("% 5");
    student.main(args);
    correct = "Enter a character:\nEnter triangle height:\n";
    correct += "\n% \n% % \n% % % \n% % % % \n% % % % % \n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test3
    setOutput();
    total++;
    setInput("m 4");
    student.main(args);
    correct = "Enter a character:\nEnter triangle height:\n";
    correct += "\nm \nm m \nm m m \nm m m m \n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }

    //hidden tests
    setOutput();
    total++;
    setInput("x 10");
    student.main(args);
    correct = "Enter a character:\nEnter triangle height:\n";
    correct += "\nx \nx x \nx x x \nx x x x \nx x x x x \nx x x x x x \nx x x x x x x \nx x x x x x x x \nx x x x x x x x x \nx x x x x x x x x x \n";
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
