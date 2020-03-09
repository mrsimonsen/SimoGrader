import java.io.*;

public class Test09 {
  static PlayerRoster student = new PlayerRoster();
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
	  setInput("1 4 6 9 21 5 47 8 83 2 q");
    student.main(args);
    String correct = "Enter player 1's jersey number:\nEnter player 1's rating:\n\nEnter player 2's jersey number:\nEnter player 2's rating:\n\nEnter player 3's jersey number:\nEnter player 3's rating:\n\nEnter player 4's jersey number:\nEnter player 4's rating:\n\nEnter player 5's jersey number:\nEnter player 5's rating:\n\n";
    correct += "ROSTER\nPlayer 1 -- Jersey number: 1, Rating: 4\nPlayer 2 -- Jersey number: 6, Rating: 9\nPlayer 3 -- Jersey number: 21, Rating: 5\nPlayer 4 -- Jersey number: 47, Rating: 8\nPlayer 5 -- Jersey number: 83, Rating: 2\n";
    String result = getOutput().substring(0,correct.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }

    //test2
    setOutput();
    total++;
    setInput("1 4 6 9 21 5 47 8 83 2 q");
    student.main(args);
    correct = "Enter player 1's jersey number:\nEnter player 1's rating:\n\nEnter player 2's jersey number:\nEnter player 2's rating:\n\nEnter player 3's jersey number:\nEnter player 3's rating:\n\nEnter player 4's jersey number:\nEnter player 4's rating:\n\nEnter player 5's jersey number:\nEnter player 5's rating:\n\n";
    correct += "ROSTER\nPlayer 1 -- Jersey number: 1, Rating: 4\nPlayer 2 -- Jersey number: 6, Rating: 9\nPlayer 3 -- Jersey number: 21, Rating: 5\nPlayer 4 -- Jersey number: 47, Rating: 8\nPlayer 5 -- Jersey number: 83, Rating: 2\n";
    result = getOutput().substring(0,correct.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
	  
    //test3
    setOutput();
    total++;
    setInput("84 7 23 4 4 5 30 2 66 9 q");
    student.main(args);
    correct = "Enter player 1's jersey number:\nEnter player 1's rating:\n\nEnter player 2's jersey number:\nEnter player 2's rating:\n\nEnter player 3's jersey number:\nEnter player 3's rating:\n\nEnter player 4's jersey number:\nEnter player 4's rating:\n\nEnter player 5's jersey number:\nEnter player 5's rating:\n";
    correct += "\nROSTER\nPlayer 1 -- Jersey number: 84, Rating: 7\nPlayer 2 -- Jersey number: 23, Rating: 4\nPlayer 3 -- Jersey number: 4, Rating: 5\nPlayer 4 -- Jersey number: 30, Rating: 2\nPlayer 5 -- Jersey number: 66, Rating: 9\n";
    correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
	  
    //test4
    setOutput();
    total++;
    setInput("84 7 23 4 4 5 30 2 66 9 o q");
    student.main(args);
    correct = "Enter player 1's jersey number:\nEnter player 1's rating:\n\nEnter player 2's jersey number:\nEnter player 2's rating:\n\nEnter player 3's jersey number:\nEnter player 3's rating:\n\nEnter player 4's jersey number:\nEnter player 4's rating:\n\nEnter player 5's jersey number:\nEnter player 5's rating:\n";
    correct += "\nROSTER\nPlayer 1 -- Jersey number: 84, Rating: 7\nPlayer 2 -- Jersey number: 23, Rating: 4\nPlayer 3 -- Jersey number: 4, Rating: 5\nPlayer 4 -- Jersey number: 30, Rating: 2\nPlayer 5 -- Jersey number: 66, Rating: 9\n";
    correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
    correct += "ROSTER\nPlayer 1 -- Jersey number: 84, Rating: 7\nPlayer 2 -- Jersey number: 23, Rating: 4\nPlayer 3 -- Jersey number: 4, Rating: 5\nPlayer 4 -- Jersey number: 30, Rating: 2\nPlayer 5 -- Jersey number: 66, Rating: 9\n";
    correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
	  
    //test5
    setOutput();
    total++;
    setInput("84 7 23 4 4 5 30 2 66 9 u 4 6 o q");
    student.main(args);
    correct = "Enter player 1's jersey number:\nEnter player 1's rating:\n\nEnter player 2's jersey number:\nEnter player 2's rating:\n\nEnter player 3's jersey number:\nEnter player 3's rating:\n\nEnter player 4's jersey number:\nEnter player 4's rating:\n\nEnter player 5's jersey number:\nEnter player 5's rating:\n";
    correct += "\nROSTER\nPlayer 1 -- Jersey number: 84, Rating: 7\nPlayer 2 -- Jersey number: 23, Rating: 4\nPlayer 3 -- Jersey number: 4, Rating: 5\nPlayer 4 -- Jersey number: 30, Rating: 2\nPlayer 5 -- Jersey number: 66, Rating: 9\n";
    correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
    correct += "Enter a jersey number:\nEnter a new rating for player:\n";
    correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
    correct += "ROSTER\nPlayer 1 -- Jersey number: 84, Rating: 7\nPlayer 2 -- Jersey number: 23, Rating: 4\nPlayer 3 -- Jersey number: 4, Rating: 6\nPlayer 4 -- Jersey number: 30, Rating: 2\nPlayer 5 -- Jersey number: 66, Rating: 9\n";
    correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
	  
    //test6
    setOutput();
    total++;
    setInput("84 7 23 4 4 5 30 2 66 9 a 4 q");
    student.main(args);
    correct = "Enter player 1's jersey number:\nEnter player 1's rating:\n\nEnter player 2's jersey number:\nEnter player 2's rating:\n\nEnter player 3's jersey number:\nEnter player 3's rating:\n\nEnter player 4's jersey number:\nEnter player 4's rating:\n\nEnter player 5's jersey number:\nEnter player 5's rating:\n";
    correct += "\nROSTER\nPlayer 1 -- Jersey number: 84, Rating: 7\nPlayer 2 -- Jersey number: 23, Rating: 4\nPlayer 3 -- Jersey number: 4, Rating: 5\nPlayer 4 -- Jersey number: 30, Rating: 2\nPlayer 5 -- Jersey number: 66, Rating: 9\n";
    correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
    correct += "Enter a rating:\n\nABOVE 4\nPlayer 1 -- Jersey number: 84, Rating: 7\nPlayer 3 -- Jersey number: 4, Rating: 5\nPlayer 5 -- Jersey number: 66, Rating: 9\n";
    correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
	  
    //test7
    setOutput();
    total++;
    setInput("12 7 47 2 33 2 19 5 90 6 a 5 q");
    student.main(args);
    correct = "Enter a rating:\n\nABOVE 5\nPlayer 1 -- Jersey number: 12, Rating: 7\nPlayer 5 -- Jersey number: 90, Rating: 6\n";
    correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
    result = getOutput();
    result = result.substring(result.length()-correct.length(),result.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
	  
    //test8
    setOutput();
    total++;
    setInput("84 7 23 4 4 5 30 2 66 9 r 66 15 6 o q");
    student.main(args);
    correct = "Enter player 1's jersey number:\nEnter player 1's rating:\n\nEnter player 2's jersey number:\nEnter player 2's rating:\n\nEnter player 3's jersey number:\nEnter player 3's rating:\n\nEnter player 4's jersey number:\nEnter player 4's rating:\n\nEnter player 5's jersey number:\nEnter player 5's rating:\n";
    correct += "\nROSTER\nPlayer 1 -- Jersey number: 84, Rating: 7\nPlayer 2 -- Jersey number: 23, Rating: 4\nPlayer 3 -- Jersey number: 4, Rating: 5\nPlayer 4 -- Jersey number: 30, Rating: 2\nPlayer 5 -- Jersey number: 66, Rating: 9\n";
    correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
    correct += "Enter a jersey number:\nEnter a new jersey number:\nEnter a rating for the new player:\n";
    correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
    correct += "ROSTER\nPlayer 1 -- Jersey number: 84, Rating: 7\nPlayer 2 -- Jersey number: 23, Rating: 4\nPlayer 3 -- Jersey number: 4, Rating: 5\nPlayer 4 -- Jersey number: 30, Rating: 2\nPlayer 5 -- Jersey number: 15, Rating: 6\n";
    correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
	  
    //test9
    setOutput();
    total++;
    setInput("84 7 23 4 4 5 30 2 66 9 r 12 o q");
    student.main(args);
    correct = "Enter player 1's jersey number:\nEnter player 1's rating:\n\nEnter player 2's jersey number:\nEnter player 2's rating:\n\nEnter player 3's jersey number:\nEnter player 3's rating:\n\nEnter player 4's jersey number:\nEnter player 4's rating:\n\nEnter player 5's jersey number:\nEnter player 5's rating:\n";
    correct += "\nROSTER\nPlayer 1 -- Jersey number: 84, Rating: 7\nPlayer 2 -- Jersey number: 23, Rating: 4\nPlayer 3 -- Jersey number: 4, Rating: 5\nPlayer 4 -- Jersey number: 30, Rating: 2\nPlayer 5 -- Jersey number: 66, Rating: 9\n";
    correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
    correct += "Enter a jersey number:\n";
    correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
    correct += "ROSTER\nPlayer 1 -- Jersey number: 84, Rating: 7\nPlayer 2 -- Jersey number: 23, Rating: 4\nPlayer 3 -- Jersey number: 4, Rating: 5\nPlayer 4 -- Jersey number: 30, Rating: 2\nPlayer 5 -- Jersey number: 66, Rating: 9\n";
    correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }


    //hidden tests
    setOutput();
    total++;
    setInput("1 1 2 2 3 3 4 4 5 5 r 5 6 6 o q");
    student.main(args);
    correct = "Enter player 1's jersey number:\nEnter player 1's rating:\n\nEnter player 2's jersey number:\nEnter player 2's rating:\n\nEnter player 3's jersey number:\nEnter player 3's rating:\n\nEnter player 4's jersey number:\nEnter player 4's rating:\n\nEnter player 5's jersey number:\nEnter player 5's rating:\n";
    correct += "\nROSTER\nPlayer 1 -- Jersey number: 1, Rating: 1\nPlayer 2 -- Jersey number: 2, Rating: 2\nPlayer 3 -- Jersey number: 3, Rating: 3\nPlayer 4 -- Jersey number: 4, Rating: 4\nPlayer 5 -- Jersey number: 5, Rating: 5\n";
    correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
    correct += "Enter a jersey number:\nEnter a new jersey number:\nEnter a rating for the new player:\n";
    correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
    correct += "ROSTER\nPlayer 1 -- Jersey number: 1, Rating: 1\nPlayer 2 -- Jersey number: 2, Rating: 2\nPlayer 3 -- Jersey number: 3, Rating: 3\nPlayer 4 -- Jersey number: 4, Rating: 4\nPlayer 5 -- Jersey number: 6, Rating: 6\n";
    correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }

    setOutput();
    total++;
    setInput("84 7 23 4 4 5 30 2 66 9 u 4 8 o q");
    student.main(args);
    correct = "Enter player 1's jersey number:\nEnter player 1's rating:\n\nEnter player 2's jersey number:\nEnter player 2's rating:\n\nEnter player 3's jersey number:\nEnter player 3's rating:\n\nEnter player 4's jersey number:\nEnter player 4's rating:\n\nEnter player 5's jersey number:\nEnter player 5's rating:\n";
    correct += "\nROSTER\nPlayer 1 -- Jersey number: 84, Rating: 7\nPlayer 2 -- Jersey number: 23, Rating: 4\nPlayer 3 -- Jersey number: 4, Rating: 5\nPlayer 4 -- Jersey number: 30, Rating: 2\nPlayer 5 -- Jersey number: 66, Rating: 9\n";
    correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
    correct += "Enter a jersey number:\nEnter a new rating for player:\n";
    correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
    correct += "ROSTER\nPlayer 1 -- Jersey number: 84, Rating: 7\nPlayer 2 -- Jersey number: 23, Rating: 4\nPlayer 3 -- Jersey number: 4, Rating: 8\nPlayer 4 -- Jersey number: 30, Rating: 2\nPlayer 5 -- Jersey number: 66, Rating: 9\n";
    correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }


    setOutput();
    total++;
    setInput("84 7 23 4 4 5 30 2 66 9 a 7 q");
    student.main(args);
    correct = "Enter player 1's jersey number:\nEnter player 1's rating:\n\nEnter player 2's jersey number:\nEnter player 2's rating:\n\nEnter player 3's jersey number:\nEnter player 3's rating:\n\nEnter player 4's jersey number:\nEnter player 4's rating:\n\nEnter player 5's jersey number:\nEnter player 5's rating:\n";
    correct += "\nROSTER\nPlayer 1 -- Jersey number: 84, Rating: 7\nPlayer 2 -- Jersey number: 23, Rating: 4\nPlayer 3 -- Jersey number: 4, Rating: 5\nPlayer 4 -- Jersey number: 30, Rating: 2\nPlayer 5 -- Jersey number: 66, Rating: 9\n";
    correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
    correct += "Enter a rating:\n\nABOVE 7\nPlayer 5 -- Jersey number: 66, Rating: 9\n";
    correct += "\nMENU\nu - Update player rating\na - Output players above a rating\nr - Replace player\no - Output roster\nq - Quit\n\nChoose an option:\n";
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
