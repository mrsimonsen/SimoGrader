import java.io.*;

public class Test02 {
  static PaintEstimator student = new PaintEstimator();
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
    setInput("10 10 ");
    student.main(args);
    String correct = "Enter wall height (feet):\nEnter wall width (feet):\nWall area: 100.0 square feet\n";
    String out = getOutput();
    String result = out.substring(0,correct.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test2
    setOutput();
    total++;
    setInput("25 14");
    student.main(args);
    correct = "Enter wall height (feet):\nEnter wall width (feet):\nWall area: 350.0 square feet\nPaint needed: 1.0 gallons\n";
    out = getOutput();
    result = out.substring(0,correct.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test3
    setOutput();
    total++;
    setInput("25.5 42");
    student.main(args);
    correct = "Enter wall height (feet):\nEnter wall width (feet):\nWall area: 1071.0 square feet\nPaint needed: 3.06 gallons\nCans needed: 4 can(s)\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }

    //hidden tests
    setOutput();
    total++;
    setInput("35 10");
    student.main(args);
    correct = "Enter wall height (feet):\nEnter wall width (feet):\nWall area: 350.0 square feet\nPaint needed: 1.0 gallons\nCans needed: 1 can(s)\n";
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
