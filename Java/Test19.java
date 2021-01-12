import java.io.*;

public class Test19 {
  static DataVisualizer student = new DataVisualizer();
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
    setInput("Number of Novels Authored\nblank\nblank\n-1\n");
    student.main(args);
    String correct = "Enter a title for the data:\nYou entered: Number of Novels Authored\n";
    String result = getOutput().substring(0,correct.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
	 
    //test2
    setOutput();
    total++;
    setInput("Number of Novels Authored\nAuthor name\nNumber of novels\n-1\n");
    student.main(args);
    correct = "Enter a title for the data:\nYou entered: Number of Novels Authored\n\n";
    correct += "Enter the column 1 header:\nYou entered: Author name\n\n";
    correct += "Enter the column 2 header:\nYou entered: Number of novels\n\n";
    result = getOutput().substring(0,correct.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
	 
    //test3
    setOutput();
    total++;
    setInput("Number of Novels Authored\nAuthor name\nNumber of novels\nJane Austen,6\n-1\n");
    student.main(args);
    correct = "Enter a title for the data:\nYou entered: Number of Novels Authored\n\n";
    correct += "Enter the column 1 header:\nYou entered: Author name\n\n";
    correct += "Enter the column 2 header:\nYou entered: Number of novels\n\n";
    correct += "Enter a data point (-1 to stop input):\nData string: Jane Austen\nData integer: 6\n";
    result = getOutput().substring(0,correct.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
	 
    //test4
    setOutput();
    total++;
    setInput("Number of Novels Authored\nAuthor name\nNumber of novels\nErnest Hemingway 9\nErnest Hemingway9\nErnest Hemingway,9\n-1\n");
    student.main(args);
    correct = "Enter a title for the data:\nYou entered: Number of Novels Authored\n\n";
    correct += "Enter the column 1 header:\nYou entered: Author name\n\n";
    correct += "Enter the column 2 header:\nYou entered: Number of novels\n\n";
    correct += "Enter a data point (-1 to stop input):\nError: No comma in string.\n\n";
    correct += "Enter a data point (-1 to stop input):\nError: No comma in string.\n\n";
    correct += "Enter a data point (-1 to stop input):\nData string: Ernest Hemingway\nData integer: 9\n";
    result = getOutput().substring(0,correct.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
	 
    //test5
    setOutput();
    total++;
    setInput("Number of Novels Authored\nAuthor name\nNumber of novels\nF, Scott Fitzgerald, 8\nF. Scott, Fitzgerald, 8\nF. Scott Fitzgerald, 8\n-1\n");
    student.main(args);
    correct = "Enter a title for the data:\nYou entered: Number of Novels Authored\n\n";
    correct += "Enter the column 1 header:\nYou entered: Author name\n\n";
    correct += "Enter the column 2 header:\nYou entered: Number of novels\n\n";
    correct += "Enter a data point (-1 to stop input):\nError: Too many commas in input.\n\n";
    correct += "Enter a data point (-1 to stop input):\nError: Too many commas in input.\n\n";
    correct += "Enter a data point (-1 to stop input):\nData string: F. Scott Fitzgerald\nData integer: 8\n";
    result = getOutput().substring(0,correct.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
	  
    //test6
    setOutput();
    total++;
    setInput("Number of Novels Authored\nAuthor name\nNumber of novels\nAgatha Christie,seventythree\nAgatha Christie,seventythree\nAgatha Christie,seventythree\nAgatha Christie,73\n-1\n");
    student.main(args);
    correct = "Enter a title for the data:\nYou entered: Number of Novels Authored\n\n";
    correct += "Enter the column 1 header:\nYou entered: Author name\n\n";
    correct += "Enter the column 2 header:\nYou entered: Number of novels\n\n";
    correct += "Enter a data point (-1 to stop input):\nError: Comma not followed by an integer.\n\n";
    correct += "Enter a data point (-1 to stop input):\nError: Comma not followed by an integer.\n\n";
    correct += "Enter a data point (-1 to stop input):\nError: Comma not followed by an integer.\n\n";
    correct += "Enter a data point (-1 to stop input):\nData string: Agatha Christie\nData integer: 73\n";
    result = getOutput().substring(0,correct.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }
	  
    //test7
    setOutput();
    total++;
    setInput("Number of Novels Authored\nAuthor name\nNumber of novels\nJane Austen,6\nCharles Dickens,20\nErnest Hemingway 9\nErnest hemingway9\nErnest Hemingway,9\nJack Kerouac,22\nF, Scott Fitzgerald,8\nF. Scott, Fitzgerald, 8\nF. Scott Fitzgerald,8\nMary Shelley,7\nCharlotte Bronte,5\nMark Twain,11\nAgatha Christie,seventythree\nAgatha Christie,seventythree\nAgatha Christie,seventythree\nAgatha Christie,73\nIan Flemming,14\nJ.K. Rowling,14\nStephen King,54\nOscar Wilde,1\n-1\n");
    student.main(args);
    correct = "Enter a title for the data:\nYou entered: Number of Novels Authored\n\n";
	correct += "Enter the column 1 header:\nYou entered: Author name\n\n";
    correct += "Enter the column 2 header:\nYou entered: Number of novels\n\n";
	correct += "Enter a data point (-1 to stop input):\nData string: Jane Austen\nData integer: 6\n\n";
	correct += "Enter a data point (-1 to stop input):\nData string: Charles Dickens\nData integer: 20\n\n";
	correct += "Enter a data point (-1 to stop input):\nError: No comma in string.\n\n";
	correct += "Enter a data point (-1 to stop input):\nError: No comma in string.\n\n";
	correct += "Enter a data point (-1 to stop input):\nData string: Ernest Hemingway\nData integer: 9\n\n";
	correct += "Enter a data point (-1 to stop input):\nData string: Jack Kerouac\nData integer: 22\n\n";
	correct += "Enter a data point (-1 to stop input):\nError: Too many commas in input.\n\n";
	correct += "Enter a data point (-1 to stop input):\nError: Too many commas in input.\n\n";
	correct += "Enter a data point (-1 to stop input):\nData string: F. Scott Fitzgerald\nData integer: 8\n\n";
	correct += "Enter a data point (-1 to stop input):\nData string: Mary Shelley\nData integer: 7\n\n";
	correct += "Enter a data point (-1 to stop input):\nData string: Charlotte Bronte\nData integer: 5\n\n";
	correct += "Enter a data point (-1 to stop input):\nData string: Mark Twain\nData integer: 11\n\n";
    correct += "Enter a data point (-1 to stop input):\nError: Comma not followed by an integer.\n\n";
	correct += "Enter a data point (-1 to stop input):\nError: Comma not followed by an integer.\n\n";
	correct += "Enter a data point (-1 to stop input):\nError: Comma not followed by an integer.\n\n";
	correct += "Enter a data point (-1 to stop input):\nData string: Agatha Christie\nData integer: 73\n\n";
	correct += "Enter a data point (-1 to stop input):\nData string: Ian Flemming\nData integer: 14\n\n";
	correct += "Enter a data point (-1 to stop input):\nData string: J.K. Rowling\nData integer: 14\n\n";
	correct += "Enter a data point (-1 to stop input):\nData string: Stephen King\nData integer: 54\n\n";
	correct += "Enter a data point (-1 to stop input):\nData string: Oscar Wilde\nData integer: 1\n\n";
	correct += "Enter a data point (-1 to stop input):\n\n";
    correct += "        Number of Novels Authored\n";
    correct += "Author name         |       Number of novels\n";
    correct += "--------------------------------------------\n";
    correct += "Jane Austen         |                      6\n";
    correct += "Charles Dickens     |                     20\n";
    correct += "Ernest Hemingway    |                      9\n";
    correct += "Jack Kerouac        |                     22\n";
    correct += "F. Scott Fitzgerald |                      8\n";
    correct += "Mary Shelley        |                      7\n";
    correct += "Charlotte Bronte    |                      5\n";
    correct += "Mark Twain          |                     11\n";
    correct += "Agatha Christie     |                     73\n";
    correct += "Ian Flemming        |                     14\n";
    correct += "J.K. Rowling        |                     14\n";
    correct += "Stephen King        |                     54\n";
    correct += "Oscar Wilde         |                      1\n";
    result = getOutput();
	//cut length of entering data
  	//result = result.substring(1832, result.length());
	//cut off end
	result = result.substring(0, correct.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }

    //test8
    setOutput();
    total++;
    setInput("Number of Novels Authored\nAuthor name\nNumber of novels\nJane Austen,6\nCharles Dickens,20\nErnest Hemingway 9\nErnest hemingway9\nErnest Hemingway,9\nJack Kerouac,22\nF, Scott Fitzgerald,8\nF. Scott, Fitzgerald, 8\nF. Scott Fitzgerald,8\nMary Shelley,7\nCharlotte Bronte,5\nMark Twain,11\nAgatha Christie,seventythree\nAgatha Christie,seventythree\nAgatha Christie,seventythree\nAgatha Christie,73\nIan Flemming,14\nJ.K. Rowling,14\nStephen King,54\nOscar Wilde,1\n-1\n");
    student.main(args);
    correct = "        Number of Novels Authored\n";
    correct += "Author name         |       Number of novels\n";
    correct += "--------------------------------------------\n";
    correct += "Jane Austen         |                      6\n";
    correct += "Charles Dickens     |                     20\n";
    correct += "Ernest Hemingway    |                      9\n";
    correct += "Jack Kerouac        |                     22\n";
    correct += "F. Scott Fitzgerald |                      8\n";
    correct += "Mary Shelley        |                      7\n";
    correct += "Charlotte Bronte    |                      5\n";
    correct += "Mark Twain          |                     11\n";
    correct += "Agatha Christie     |                     73\n";
    correct += "Ian Flemming        |                     14\n";
    correct += "J.K. Rowling        |                     14\n";
    correct += "Stephen King        |                     54\n";
    correct += "Oscar Wilde         |                      1\n\n";
    correct += "         Jane Austen ******\n";
    correct += "     Charles Dickens ********************\n";
    correct += "    Ernest Hemingway *********\n";
    correct += "        Jack Kerouac **********************\n";
    correct += " F. Scott Fitzgerald ********\n";
    correct += "        Mary Shelley *******\n";
    correct += "    Charlotte Bronte *****\n";
    correct += "          Mark Twain ***********\n";
    correct += "     Agatha Christie *************************************************************************\n";
    correct += "        Ian Flemming **************\n";
    correct += "        J.K. Rowling **************\n";
    correct += "        Stephen King ******************************************************\n";
    correct += "         Oscar Wilde *\n";
    result = getOutput();
    result = result.substring(result.length()-correct.length(),result.length());
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }

    //hidden test
    setOutput();
    total++;
    setInput("Ages of Simonsens\nName\nAge\nJohn Simonsen, 31\nTeresa Simonsen, 32\nEmily Simonsen, 4\n-1\n");
    student.main(args);
    correct = "Enter a title for the data:\nYou entered: Ages of Simonsens\n\nEnter the column 1 header:\nYou entered: Name\n\nEnter the column 2 header:\nYou entered: Age\n\nEnter a data point (-1 to stop input):\nData string: John Simonsen\nData integer: 31\n\nEnter a data point (-1 to stop input):\nData string: Teresa Simonsen\nData integer: 32\n\nEnter a data point (-1 to stop input):\nData string: Emily Simonsen\nData integer: 4\n\nEnter a data point (-1 to stop input):\n\n";
    correct += "                Ages of Simonsens\n";
    correct += "Name                |                    Age\n";
    correct += "--------------------------------------------\n";
    correct += "John Simonsen       |                     31\n";
    correct += "Teresa Simonsen     |                     32\n";
    correct += "Emily Simonsen      |                      4\n\n";
    correct += "       John Simonsen *******************************\n";
    correct += "     Teresa Simonsen ********************************\n";
    correct += "      Emily Simonsen ****\n";
    result = getOutput();
    restoreSystem();
    if (result.equals(correct)){
      score++;
    }

    total++;
    setOutput();
    setInput("Ages of Simonsens\nName\nAge\nJohn Simonsen, 27\nTeresa Simonsen, 28\nEmily Simonsen, 0\n-1\n");
    student.main(args);
    correct = "Enter a title for the data:\nYou entered: Ages of Simonsens\n\nEnter the column 1 header:\nYou entered: Name\n\nEnter the column 2 header:\nYou entered: Age\n\nEnter a data point (-1 to stop input):\nData string: John Simonsen\nData integer: 27\n\nEnter a data point (-1 to stop input):\nData string: Teresa Simonsen\nData integer: 28\n\nEnter a data point (-1 to stop input):\nData string: Emily Simonsen\nData integer: 0\n\nEnter a data point (-1 to stop input):\n\n";
    correct += "                Ages of Simonsens\n";
    correct += "Name                |                    Age\n";
    correct += "--------------------------------------------\n";
    correct += "John Simonsen       |                     27\n";
    correct += "Teresa Simonsen     |                     28\n";
    correct += "Emily Simonsen      |                      0\n\n";
    correct += "       John Simonsen ***************************\n";
    correct += "     Teresa Simonsen ****************************\n";
    correct += "      Emily Simonsen \n";
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
