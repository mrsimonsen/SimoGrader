public class Test17 {
  static BinConverter student = new BinConverter();

  public static void main(String[] args){
    System.out.println(tests());
  }

  public static String tests(){
    int total = 0;
    int score = 0;
    //test1
    total++;
    String result = student.convert(14);
    String correct = "1110";
    if (result.equals(correct)){
      score++;
    }
    //test2
    total++;
    result = student.convert(255);
    correct = "1111 1111";
    if (result.equals(correct)){
      score++;
    }
    //test3
    total++;
    result = student.convert(109);
    correct = "0110 1101";
    if (result.equals(correct)){
      score++;
    }
    //test4
    total++;
    result = student.convert(3000);
    correct = "1011 1011 1000";
    if (result.equals(correct)){
      score++;
    }

    //hidden tests
    total++;
    result = student.convert(213);
    correct = "1101 0101";
    if (result.equals(correct)){
      score++;
    }

    //testing complete
    String rep = ""+ score +"/"+total;
    return rep;
  }
}
