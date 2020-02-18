public class Test12 {
  static DiceStats student = new DiceStats();

  public static void main(String[] args){
    System.out.println(tests());
  }

  public static String tests(){
    int total = 0;
    int score = 0;
    //test1
    total++;
    boolean result = student.cont(1);
    if (result){
      score++;
    }
    //test2
    total++;
    result = student.cont(0);
    if (!result){
      score++;
    }
    //test3
    total++;
    result = student.cont(10);
    if (result){
      score++;
    }
    //test4
    total++;
    int[] totals = {1,1,1,1,1,1,1,1,1,1,1};
    String c = "Dice roll histogram:\n\n";
    String star = "*\n";
    c += "2:  "+star;
    c += "3:  "+star;;
    c += "4:  "+star;;
    c += "5:  "+star;
    c += "6:  "+star;
    c += "7:  "+star;
    c += "8:  "+star;
    c += "9:  "+star;
    c += "10: "+star;
    c += "11: "+star;
    c += "12: "+star;
    String r = student.histogram(totals);
    if (r.equals(c)){
      score++;
    }
    //test5
    total++;
    int[] total2 = {4,4,4,4,4,4,4,4,4,4,4};
    c = "Dice roll histogram:\n\n";
    star = "****\n";
    c += "2:  "+star;
    c += "3:  "+star;;
    c += "4:  "+star;;
    c += "5:  "+star;
    c += "6:  "+star;
    c += "7:  "+star;
    c += "8:  "+star;
    c += "9:  "+star;
    c += "10: "+star;
    c += "11: "+star;
    c += "12: "+star;

    r = student.histogram(total2);
    if (r.equals(c)){
      score++;
    }
    //test6
    total++;
    int[] total3 = {2,3,5,3,3,3,5,8,4,1,3};
    c = "Dice roll histogram:\n\n";
    c += "2:  **\n";
    c += "3:  ***\n";
    c += "4:  *****\n";
    c += "5:  ***\n";
    c += "6:  ***\n";
    c += "7:  ***\n";
    c += "8:  *****\n";
    c += "9:  ********\n";
    c += "10: ****\n";
    c += "11: *\n";
    c += "12: ***\n";

    r = student.histogram(total3);
    if (r.equals(c)){
      score++;
    }

    //hidden tests
    total++;
    int[] total4 = {1,2,3,4,5,6,7,8,9,10,11};
    c = "Dice roll histogram:\n\n";
    c += "2:  *\n";
    c += "3:  **\n";
    c += "4:  ***\n";
    c += "5:  ****\n";
    c += "6:  *****\n";
    c += "7:  ******\n";
    c += "8:  *******\n";
    c += "9:  ********\n";
    c += "10: *********\n";
    c += "11: **********\n";
    c += "12: ***********\n";

    r = student.histogram(total4);
    if (r.equals(c)){
      score++;
    }

    total++;
    int[] total6 = {12,10,9,8,7,6,5,4,3,2};
    c = "Dice roll histogram:\n\n";
    c += "2:  ***********\n";
    c += "3:  **********\n";
    c += "4:  *********\n";
    c += "5:  ********\n";
    c += "6:  *******\n";
    c += "7:  ******\n";
    c += "8:  *****\n";
    c += "9:  ****\n";
    c += "10: ***\n";
    c += "11: **\n";
    c += "12: *\n";
    r = student.histogram(total6);
    if (r.equals(c)){
      score++;
    }

    //testing complete
    String rep = ""+ score +"/"+total;
    return rep;
  }
}
