import java.io.*;

public class Test03 {
  static TextMsgAbbreviation student = new TextMsgAbbreviation();
  static private ByteArrayOutputStream TOut;
  private static ByteArrayInputStream TIn;
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
    setInput("LOL");
    student.main(args);
    String correct = "Input an abbreviation:\nlaughing out loud\n";
    String result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test2
    setOutput();
    total++;
    setInput("IDK");
    student.main(args);
    correct = "Input an abbreviation:\nI don't know\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test3
    setOutput();
    total++;
    setInput("XYZ");
    student.main(args);
    correct = "Input an abbreviation:\nUnknown\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test4
    setOutput();
    total++;
    setInput("BFF");
    student.main(args);
    correct = "Input an abbreviation:\nbest friends forever\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test5
    setOutput();
    total++;
    setInput("IMH");
    student.main(args);
    correct = "Input an abbreviation:\nUnknown\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test6
    setOutput();
    total++;
    setInput("IMHO");
    student.main(args);
    correct = "Input an abbreviation:\nin my humble opinion\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test7
    setOutput();
    total++;
    setInput("TMI");
    student.main(args);
    correct = "Input an abbreviation:\ntoo much information\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }

    //no hidden tests for 03
    //testing complete
    String rep = ""+ score +"/"+total;
    return rep;
  }

  //Set up methods
  static public void setOutput(){
    TOut = new ByteArrayOutputStream();
    System.setOut(new PrintStream(TOut));
  }
  static private void setInput(String data){
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
