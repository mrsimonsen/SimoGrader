import java.io.*;
import java.util.Scanner;

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
    //test2a
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
	//test2b
	total++;
	Scanner s = new Scanner("1\nq\n");
	char res = student.printMenu(s);
	char cor = 'q';
	if (res == cor){
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
	
	//test 8
	total++;
	setOutput();
	  setInput("We'll continue our quest in space.  There will be more shuttle flights and more shuttle crews and,  yes,  more volunteers, more civilians,  more teachers in space.  Nothing ends here;  our hopes and our journeys continue!\nc\nw\nf\nmore\nr\ns\nq\n");
		correct = "Enter a sample text:\n\nYou entered: We'll continue our quest in space.  There will be more shuttle flights and more shuttle crews and,  yes,  more volunteers, more civilians,  more teachers in space.  Nothing ends here;  our hopes and our journeys continue!\n";
   		correct += "\nMENU\nc - Number of non-whitespace characters\nw - Number of words\nf - Find text\nr - Replace all !\'s\ns - Shorten spaces\nq - Quit\n\nChoose an option:\n";
		correct += "Number of non-whitespace characters: 181\n";
		correct += "\nMENU\nc - Number of non-whitespace characters\nw - Number of words\nf - Find text\nr - Replace all !\'s\ns - Shorten spaces\nq - Quit\n\nChoose an option:\n";
		correct += "Number of words: 35\n";
		correct += "\nMENU\nc - Number of non-whitespace characters\nw - Number of words\nf - Find text\nr - Replace all !\'s\ns - Shorten spaces\nq - Quit\n\nChoose an option:\n";
		correct += "Enter a word or phrase to be found:\n\"more\" instances: 5\n";
		correct += "\nMENU\nc - Number of non-whitespace characters\nw - Number of words\nf - Find text\nr - Replace all !\'s\ns - Shorten spaces\nq - Quit\n\nChoose an option:\n";
		correct += "Edited text: We'll continue our quest in space.  There will be more shuttle flights and more shuttle crews and,  yes,  more volunteers, more civilians,  more teachers in space.  Nothing ends here;  our hopes and our journeys continue.\n";
		correct += "\nMENU\nc - Number of non-whitespace characters\nw - Number of words\nf - Find text\nr - Replace all !\'s\ns - Shorten spaces\nq - Quit\n\nChoose an option:\n";
		correct += "Edited text: We'll continue our quest in space. There will be more shuttle flights and more shuttle crews and, yes, more volunteers, more civilians, more teachers in space. Nothing ends here; our hopes and our journeys continue.\n";
		correct += "\nMENU\nc - Number of non-whitespace characters\nw - Number of words\nf - Find text\nr - Replace all !\'s\ns - Shorten spaces\nq - Quit\n\nChoose an option:\n";
		student.main(args);
		result = getOutput();
	  if (result.equals(correct)){
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
  public static void toFile(String correct, String result){
	try{
		File c = new File("correct.txt");
		File r = new File("result.txt");
		PrintWriter wc = new PrintWriter(c);
		wc.print(correct);
		wc.close();
		PrintWriter wr = new PrintWriter(r);
		wr.print(result);
		wr.close();
	}
	catch (FileNotFoundException e){
		System.out.println("Couldn't create files.");
		System.out.println(e);
	}
  }
}
