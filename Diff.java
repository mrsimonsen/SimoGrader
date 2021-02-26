import java.util.Arrays;
import java.util.ArrayList;

public class Diff{
  public static final String CHECK = "\u2714";
  public static final String CROSS = "\u274C";
  //text color
	public static final String RESET = "\u001B[0m";
	public static final String BLACK = "\u001B[30m";
	public static final String RED = "\u001B[31m";
	public static final String GREEN = "\u001B[32m";
	public static final String YELLOW = "\u001B[33m";
	public static final String BLUE = "\u001B[34m";
	public static final String PURPLE = "\u001B[35m";
	public static final String CYAN = "\u001B[36m";
	public static final String WHITE = "\u001B[37m";
	//background color
	public static final String BLACK_BACKGROUND = "\u001B[40m";
	public static final String RED_BACKGROUND = "\u001B[41m";
	public static final String GREEN_BACKGROUND = "\u001B[42m";
	public static final String YELLOW_BACKGROUND = "\u001B[43m";
	public static final String BLUE_BACKGROUND = "\u001B[44m";
	public static final String PURPLE_BACKGROUND = "\u001B[45m";
	public static final String CYAN_BACKGROUND = "\u001B[46m";
	public static final String WHITE_BACKGROUND = "\u001B[47m";

//compare ints
  public static String comapre(String testName, int result, int correct){
		if(result == correct){
      return GREEN+CHECK+"  "+testName+" Passed"+RESET;
    }
 		return RED+CROSS+"  "+testName+" Failed"+RESET+"\n\tExpected: "+correct+"\n\tBut was: "+result;
  }
//compare bools
	public static String compare(String testName, boolean result, boolean correct){
		if(result == correct){
      return GREEN+CHECK+"  "+testName+" Passed"+RESET;
    }
 		return RED+CROSS+"  "+testName+" Failed"+RESET+"\n\tExpected: "+correct+"\n\tBut was: "+result;
	}
//compare char
	public static String compare(String testName,char result, char correct){
		if(result == correct){
      return GREEN+CHECK+"  "+testName+" Passed"+RESET;
    }
 		return RED+CROSS+"  "+testName+" Failed"+RESET+"\n\tExpected: "+correct+"\n\tBut was: "+result;
	}
//compare int[]
	public static String compare(String testName, int[] result, int[] correct){
		if(Arrays.equals(result, correct)){
			return GREEN+CHECK+"  "+testName+" Passed"+RESET;
		}
		return RED+CROSS+"  "+testName+" Failed"+RESET+"\n"+diff(result,correct);
	}

	public static String diff(int[] result, int[] correct){
		if (result.length != correct.length){
			return "\tArray lengths differ!\n\tExpected: "+correct.length+" elements\n\tBut was: "+result.length+" elements";
		}
		for(int i = 0; i<correct.length;i++){
			if(correct[i]!=result[i]){
				return "\tArrays differ at index "+i+"\n\tExpected: "+correct[1]+"\n\tBut was: "+result[i];
			}
		}
		return "error comparing int[]";
	}
//compare string[]
	public static String compare(String testName, String[] result, String[] correct){
			if(Arrays.equals(result, correct)){
				return GREEN+CHECK+"  "+testName+" Passed"+RESET;
			}
			return RED+CROSS+"  "+testName+" Failed"+RESET+"\n"+diff(result,correct);
		}

		public static String diff(String[] result, String[] correct){
			if (result.length != correct.length){
				return "\tArray lengths differ!\n\tExpected: "+correct.length+" elements\n\tBut was: "+result.length+" elements";
			}
			for(int i = 0; i<correct.length;i++){
				if(!correct[i].equals(result[i])){
					return "\tArrays differ at index "+i+"\n\tExpected: "+correct[1]+"\n\tBut was: "+result[i];
				}
			}
			return "error comparing int[]";
		}
//compare strings
		public static String compare(String testName, String result, String correct){
		if(result.equals(correct)){
			return GREEN+CHECK+"  "+testName+" Passed"+RESET;
		}
		String r = RED+CROSS+"  "+testName+" Failed"+RESET+"\n";
		r += diff(result, correct);
		return r;
	}

	public static ArrayList<String> splitter (String thing){
		ArrayList<String> list = new ArrayList<String>();
		int last = 0;
		for (int i=0; i<thing.length();i++){
			if(thing.charAt(i) == '\n'){
				list.add(thing.substring(last, i)+"\n");
				last = i+1;
			}
		}
		if(list.size()<1){
			list.add(thing);
		}
		return list;
	}

	public static int[] locate(ArrayList<String> rList, ArrayList<String> cList){
		//iterate through the lines until the first difference
		for(int line = 0; line < rList.size() && line < cList.size();line++){
			for(int index = 0; index < rList.get(line).length() && index < cList.get(line).length();index++){
				//stop if the characters don't match
				if (rList.get(line).charAt(index) != cList.get(line).charAt(index)) {
					int[] locations = {line,index};
					return locations;
				}
			}
		}
		int[] notFound = {-1,-1};
		return notFound;
	}

	public static String convertChar(char current){
		String converted = "";
		if(Character.isWhitespace(current)){
			switch(current){
				case '\t':
					converted += "\\t";
					break;
				case '\n':
					converted += "\\n";
					break;
				case '\r':
					converted += "\\r";
					break;
				default:
					converted += current;
			}
		}
		else{
			converted += current;
		}
		return converted;
	}

	public static void convertLines(ArrayList<String> lines){
		String converted;
		String line;
		for(int i = 0;i<lines.size();i++){
			converted = "";
			line = lines.get(i);
			for(int j = 0; j<line.length();j++){
				converted += convertChar(line.charAt(j));
			}
			lines.set(i,converted);
		}
	}

	public static String getDiff(ArrayList<String> lines, int line, int index){
		String diff = "";
		diff += lines.get(line).charAt(index);
		if (diff.equals("\\")){
			diff += lines.get(line).charAt(index+1);
		}
		return diff;
	}

	public static String color(String line, int index, String rdiff){
	String highlight = BLUE_BACKGROUND+RED+line.substring(0,index);
	highlight += BLACK_BACKGROUND+WHITE + rdiff + BLUE_BACKGROUND+RED;
	highlight += line.substring(index + rdiff.length(),line.length())+RESET;
	return highlight;
	}

	public static String diff(String result, String correct) {
		int line;//line number
		int index;//index of different character in the line
		String message = "";//helpful display message for students
		String cdiff = "";//what the character was supposed to be
		String rdiff = "";//what the character was

		//split both strings into arrays at \n but keep the newline
		ArrayList<String> rList = splitter(result);
		ArrayList<String> cList = splitter(correct);

		//convert lines to use escape characters for whitespace
		convertLines(rList);
		convertLines(cList);
	
		//find the line and index number of the first difference
		int[] temp = locate(rList,cList);
		line = temp[0];
		index = temp[1];

		//if the strings were different
		if (index >= 0 && line >= 0) {
			//get the different characters
			cdiff = getDiff(cList, line, index);
			rdiff = getDiff(rList, line, index);
			
			//Add color to affected line- https://stackoverflow.com/questions/5762491/how-to-print-color-in-console-using-system-out-println
			String highlight = color(rList.get(line),index,rdiff);
			//make the message
			message += "Expected '"+cdiff+"', but was '"+rdiff+"'\n";
			message += "On line "+line+", index "+index+"\n";
			message += "Context:\n";
			String[] context = {"","","",""};
			if(line > 0){
				context[0] ="Line "+(line-1)+": "+ rList.get(line-1);
			}
			context[1] = "Line "+(line)+": "+highlight;
			String mark = " ";
			for(int i=0; i<rList.get(line).length(); i++){
				if(i == index){
					mark += "^";
				}
				else{
					mark += " ";	
				}
			}
			context[2] = "       "+mark;
			if(line < (rList.size()-1)){
				context[3] = "Line "+(line+1)+": "+rList.get(line+1);
			}
			for(String in: context){
				if(in.length()>0){
					message += in+"\n";
				}
			}
		}
		else{
			message = "";
		}
		return message;
	}


//testing
  public static void main(String[] args){
	String[] x = {"abc","d","e"};
	String[] y = {"abc","fun","e"};
  System.out.println(compare("sample1",x,x));
  System.out.println(compare("sample2",x,y));
  }
}