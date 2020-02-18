public class Test10 {
  static CoinFlipper student = new CoinFlipper();

  public static void main(String[] args){
    System.out.println(tests());
  }

  public static String tests(){
    int total = 0;
    int score = 0;
    //test1
    total++;
    int result = student.flipper(10,0);
    if (result==3||result==7){
      score++;
    }
    //test2
    total++;
    result = student.flipper(500,14);
    if (result==255||result==245){
      score++;
    }

    //hidden tests
    total++;
    result = student.flipper(250,0);
    if (result==122||result==128){
      score++;
    }

    //testing complete
    String rep = ""+ score +"/"+total;
    return rep;
  }
}
