public class Test11 {
  static ReverseMessage student = new ReverseMessage();

  public static void main(String[] args){
    System.out.println(tests());
  }

  public static String tests(){
    int total = 0;
    int score = 0;
    //test1
    total++;
    String message = "This is a message.";
    String result = student.reverse(message);
    String correct = ".egassem a si sihT";
    if (result.equals(correct)){
      score++;
    }
    //test2
    total++;
    message = "You miss Python, don't you?";
    result = student.reverse(message);
    correct = "?uoy t'nod ,nohtyP ssim uoY";
    if (result.equals(correct)){
      score++;
    }

    //hidden tests
    total++;
    message = "Simonsen";
    result = student.reverse(message);
    correct = "nesnomiS";
    if (result.equals(correct)){
      score++;
    }

    //testing complete
    String rep = ""+ score +"/"+total;
    return rep;
  }
}
