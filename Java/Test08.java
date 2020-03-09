import java.io.*;

public class Test08 {
  static PeopleWeights student = new PeopleWeights();
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
    setInput("236.0 89.5 142.0 166.3 93.0");
    student.main(args);
    String correct = "Enter weight 1:\nEnter weight 2:\nEnter weight 3:\nEnter weight 4:\nEnter weight 5:\n";
    correct += "You entered: 236.0 89.5 142.0 166.3 93.0 \n";
    String result = getOutput().substring(0,correct.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test2
    setOutput();
    total++;
    setInput("123.4 56.0 98.0 174.0 215.8");
    student.main(args);
    correct = "Enter weight 1:\nEnter weight 2:\nEnter weight 3:\nEnter weight 4:\nEnter weight 5:\n";
    correct += "You entered: 123.4 56.0 98.0 174.0 215.8 \n";
    result = getOutput().substring(0,correct.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test3
    setOutput();
    total++;
    setInput("236.0 89.5 142.0 166.3 93.0");
    student.main(args);
    correct = "Enter weight 1:\nEnter weight 2:\nEnter weight 3:\nEnter weight 4:\nEnter weight 5:\n";
    correct += "You entered: 236.0 89.5 142.0 166.3 93.0 \n";
    correct += "\nTotal weight: 726.8\n";
    result = getOutput().substring(0,correct.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test4
    setOutput();
    total++;
    setInput("236.0 89.5 142.0 166.3 93.0");
    student.main(args);
    correct = "Enter weight 1:\nEnter weight 2:\nEnter weight 3:\nEnter weight 4:\nEnter weight 5:\n";
    correct += "You entered: 236.0 89.5 142.0 166.3 93.0 \n";
    correct += "\nTotal weight: 726.8\n";
    correct += "Average weight: 145.35999999999999\n";
    result = getOutput().substring(0,correct.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test5
    setOutput();
    total++;
    setInput("236.0 89.5 142.0 166.3 93.0");
    student.main(args);
    correct = "Enter weight 1:\nEnter weight 2:\nEnter weight 3:\nEnter weight 4:\nEnter weight 5:\n";
    correct += "You entered: 236.0 89.5 142.0 166.3 93.0 \n";
    correct += "\nTotal weight: 726.8\n";
    correct += "Average weight: 145.35999999999999\n";
    correct += "Max weight: 236.0\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test6
    setOutput();
    total++;
    setInput("123.4 56.0 98.0 174.0 215.8");
    student.main(args);
    correct = "Enter weight 1:\nEnter weight 2:\nEnter weight 3:\nEnter weight 4:\nEnter weight 5:\n";
    correct += "You entered: 123.4 56.0 98.0 174.0 215.8 \n";
    correct += "\nTotal weight: 667.2\n";
    correct += "Average weight: 133.44\n";
    correct += "Max weight: 215.8\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }

    //hidden tests
    setOutput();
    total++;
    setInput("1.2 3.5 6.7 8.9 0.0");
    student.main(args);
    correct = "Enter weight 1:\nEnter weight 2:\nEnter weight 3:\nEnter weight 4:\nEnter weight 5:\n";
    correct += "You entered: 1.2 3.5 6.7 8.9 0.0 \n";
    correct += "\nTotal weight: 20.3\n";
    correct += "Average weight: 4.0600000000000005\n";
    correct += "Max weight: 8.9\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }

    setOutput();
    total++;
    setInput("60 60 20 50 70");
    student.main(args);
    correct = "Enter weight 1:\nEnter weight 2:\nEnter weight 3:\nEnter weight 4:\nEnter weight 5:\n";
    correct += "You entered: 60.0 60.0 20.0 50.0 70.0 \n";
    correct += "\nTotal weight: 260.0\n";
    correct += "Average weight: 52.0\n";
    correct += "Max weight: 70.0\n";
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
