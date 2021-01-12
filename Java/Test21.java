import java.util.Scanner;
import java.util.Random;
import java.util.Arrays;
import java.io.*;

public class Test21 {
  static Yahtzee student = new Yahtzee();
  static private ByteArrayOutputStream TOut;
  static private ByteArrayInputStream TIn;
  static private final PrintStream SOut = System.out;
  static private final InputStream SIn = System.in;

  public static void main(String[] args){
    System.out.println(tests());
  }

  public static String tests(){
    int total = 0;
    int score = 0;
    //test1
    total++;
    String input = "30 4";
    Scanner s = new Scanner(input);
    int r = student.holding(s);
    if (r==4){
      score++;
    }
    //test2
    total++;
    input = "0";
    s = new Scanner(input);
    r = student.holding(s);
    if (r==0){
      score++;
    }
    //test3
    total++;
    input = " 14 1 ";
    s = new Scanner(input);
    Random rand = new Random();
    int[] start = {1,2,3,4,5};
    rand.setSeed(0);
    int[] c = {1,2,3,4,5};
    int[] r3 = student.rerollDice(start,s,rand,4);
    if (Arrays.equals(r3,c)){
      score++;
    }
    //test4
    total++;
    input = " 14 1 3 5 ";
    s = new Scanner(input);
    rand = new Random();
    int[] start4 = {1,2,3,4,5};
    rand.setSeed(25);
    int[] c4 = {6,2,1,4,6};
    int[] r4 = student.rerollDice(start4,s,rand,2);
    if (Arrays.equals(r4,c4)){
      score++;
    }
    //test5
    total++;
    int[] g = {1,2,3,4,5};
    String result = student.printDice(g);
    String wspace = "1 2 3 4 5 ";
    String wospace = "1 2 3 4 5";
    if (result.equals(wspace)||result.equals(wospace)){
      score++;
    }
    //test6
    total++;
    int[] h = {5,4,3,2,1};
    result = student.printDice(h);
    wspace = "5 4 3 2 1 ";
    wospace = "5 4 3 2 1";
    if (result.equals(wspace)||result.equals(wospace)){
      score++;
    }
    //test7
    total++;
    int[] j = {1,1,3,5,6};
    int[] c7 = {2,0,1,0,1,1};
    int[] r7 = student.kinds(j);
    if (Arrays.equals(c7,r7)){
      score++;
    }
    //test8
    total++;
    int[] k = {2,3,4,4,6};
    int[] c8 = {0,1,1,2,0,1};
    int[] r8 = student.kinds(k);
    if (Arrays.equals(c8,r8)){
      score++;
    }
    //test9
    total++;
    //6 possible Yahtzees
    int[][] dice9 = {{4,4,4,4,4},{6,6,6,6,6},{5,5,5,5,5},{3,3,3,3,3},{2,2,2,2,2},{1,1,1,1,1}};
    String correct = "Yahtzee";
    String[] c9 = new String[dice9.length];
    for (int i = 0; i<dice9.length; i++){
      c9[i] = correct;
    }
    String[] r9 = new String[dice9.length];
    for (int i = 0; i < dice9.length; i++){
        r9[i] = student.printScore(dice9[i]);
      }
      if (Arrays.equals(c9,r9)){
        score++;
      }
      //test10
      total++;
    //2 possible Large Straights
    int[][] dice10 = {{4,5,6,3,2},{5,2,4,1,3}};
    correct = "Large Straight";
    String[] c10 = new String[dice10.length];
    for (int i = 0; i<dice10.length; i++){
      c10[i] = correct;
    }
    String[] r10 = new String[dice10.length];
    for (int i = 0; i < dice10.length; i++){
        r10[i] = student.printScore(dice10[i]);
      }
      if (Arrays.equals(c10,r10)){
        score++;
      }
      //test11
      total++;
    //14 possible Small Straights
    int[][] dice11 = {
      {1,2,3,4,6},{1,2,3,4,1},{1,2,3,4,2},{1,2,3,4,3},{1,2,3,4,4},
      {2,3,4,5,2},{2,3,4,5,3},{2,3,4,5,4},{2,3,4,5,5},
      {3,4,5,6,6},{3,4,5,6,1},{3,4,5,6,3},{3,4,5,6,4},{3,4,5,6,5}
    };
    correct = "Small Straight";
    String[] c11 = new String[dice11.length];
    for (int i = 0; i<dice11.length; i++){
      c11[i] = correct;
    }
    String[] r11 = new String[dice11.length];
    for (int i = 0; i < dice11.length; i++){
        r11[i] = student.printScore(dice11[i]);
      }
      if (Arrays.equals(c11,r11)){
        score++;
      }
      //test12
      total++;
    //testing 2 of the possible 4 o' Kinds
    int[][] dice12 = {{4,4,3,4,4},{3,3,3,5,3}};
    correct = "Four of a Kind";
    String[] c12 = new String[dice12.length];
    for (int i = 0; i<dice12.length; i++){
      c12[i] = correct;
    }
    String[] r12 = new String[dice12.length];
    for (int i = 0; i < dice12.length; i++){
        r12[i] = student.printScore(dice12[i]);
      }
      if (Arrays.equals(c12,r12)){
        score++;
      }
      //test13
      total++;
    //testing 3 of the possible full houses
    int[][] dice13 = {{2,2,3,3,3},{4,4,4,6,6},{1,4,1,4,1}};
    correct = "Full House";
    String[] c13 = new String[dice13.length];
    for (int i = 0; i<dice13.length; i++){
      c13[i] = correct;
    }
    String[] r13 = new String[dice13.length];
    for (int i = 0; i < dice13.length; i++){
        r13[i] = student.printScore(dice13[i]);
      }
      if (Arrays.equals(c13,r13)){
        score++;
      }
      //test14
      total++;
    //testing 2 of the possible 3 o' kinds
    int[][] dice14 = {{4,4,4,1,2},{1,3,5,3,3}};
    correct = "Three of a Kind";
    String[] c14 = new String[dice14.length];
    for (int i = 0; i<dice14.length; i++){
      c14[i] = correct;
    }
    String[] r14 = new String[dice14.length];
    for (int i = 0; i < dice14.length; i++){
        r14[i] = student.printScore(dice14[i]);
      }
      if (Arrays.equals(c14,r14)){
        score++;
      }
      //test15
      total++;
    //testing 2 of the possible no score
    int[][] dice15 = {{1,1,4,5,3},{6,5,3,5,6}};
    correct = "You did not score anything noteworthy.";
    String[] c15 = new String[dice15.length];
    for (int i = 0; i<dice15.length; i++){
      c15[i] = correct;
    }
    String[] r15 = new String[dice15.length];
    for (int i = 0; i < dice15.length; i++){
        r15[i] = student.printScore(dice15[i]);
      }
      if (Arrays.equals(c15,r15)){
        score++;
      }

      //no hidden tests
      //testing complete
      String rep = "" + score +"/"+total;
      return rep;
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
