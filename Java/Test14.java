import java.io.*;

public class Test14 {
  static AuthoringAssistant student = new AuthoringAssistant();
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
    setInput("Testing that enterd text is repeated.\nq\n");
    student.main(args);
    String correct = "Enter a sample text:\n\nYou entered: Testing that enterd text is repeated.\n";
    String result = getOutput().substring(0,correct.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test2
    setOutput();
    total++;
    setInput("Testing that menu is called and can quit.\nq\n");
    student.main(args);
    correct = "";
    correct += "Enter a sample text:\n\nYou entered: Testing that menu is called and can quit.\n";
    correct += "\nMENU\nc - Number of non-whitespace characters\nw - Number of words\nf - Find text\nr - Replace all !\'s\ns - Shorten spaces\nq - Quit\n\nChoose an option:\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
    //test3
    total++;
    int r = student.getNumOfNonWSCharacters("This is a   test.");
    if (r==12){
      score++;
    }
    //test4
    total++;
    r = student.getNumOfWords("This is a   test.");
    if (r==4){
      score++;
    }
    //test5
    total++;
    r = student.findText("some water", "I want some water. I had some water earlier, but now he has some water.");
    if (r==3){
      score++;
    }
    //test6
    total++;
    result = student.replaceExclamation("May the Force be with  you!");
    if (result.equals("May the Force be with  you.")){
      score++;
    }
    //test7
    total++;
    result = student.shortenSpace("             There are  too  many    spaces     here.      Why?");
    if (result.equals("There are too many spaces here. Why?")){
      score++;
    }

    //hidden tests
    setOutput();
    total++;
		setInput("I have a test! I am not prepared!\nr\nw\nc\nq\n");
    student.main(args);
    correct = "Enter a sample text:\n\nYou entered: I have a test! I am not prepared!\n";
    correct += "\nMENU\nc - Number of non-whitespace characters\nw - Number of words\nf - Find text\nr - Replace all !\'s\ns - Shorten spaces\nq - Quit\n\nChoose an option:\n";
    correct += "Edited text: I have a test. I am not prepared.\n";
    correct += "\nMENU\nc - Number of non-whitespace characters\nw - Number of words\nf - Find text\nr - Replace all !\'s\ns - Shorten spaces\nq - Quit\n\nChoose an option:\n";
		correct += "Number of words: 8\n";
		correct += "\nMENU\nc - Number of non-whitespace characters\nw - Number of words\nf - Find text\nr - Replace all !\'s\ns - Shorten spaces\nq - Quit\n\nChoose an option:\n";
		correct += "Number of non-whitespace characters: 26\n";
		correct += "\nMENU\nc - Number of non-whitespace characters\nw - Number of words\nf - Find text\nr - Replace all !\'s\ns - Shorten spaces\nq - Quit\n\nChoose an option:\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }

    setOutput();
    total++;
    setInput("I want some water. I had some water earlier, but now he has some water   .\nf\nsome water\ns\nq\n");
    student.main(args);
    correct = "";
    correct = "Enter a sample text:\n\nYou entered: I want some water. I had some water earlier, but now he has some water   .\n";
    correct += "\nMENU\nc - Number of non-whitespace characters\nw - Number of words\nf - Find text\nr - Replace all !\'s\ns - Shorten spaces\nq - Quit\n\nChoose an option:\n";
    correct += "Enter a word or phrase to be found:\n\"some water\" instances: 3\n";
    correct += "\nMENU\nc - Number of non-whitespace characters\nw - Number of words\nf - Find text\nr - Replace all !\'s\ns - Shorten spaces\nq - Quit\n\nChoose an option:\n";
		correct += "Edited text: I want some water. I had some water earlier, but now he has some water .\n";
		correct += "\nMENU\nc - Number of non-whitespace characters\nw - Number of words\nf - Find text\nr - Replace all !\'s\ns - Shorten spaces\nq - Quit\n\nChoose an option:\n";
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
