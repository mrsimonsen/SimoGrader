import java.util.ArrayList;

public class Diff{
	public static ArrayList<String> splitter (String thing){
		ArrayList<String> list = new ArrayList<String>();
		int last = 0;
		for (int i=0; i<thing.length();i++){
			if(thing.charAt(i) == '\n'){
				list.add(thing.substring(last, i)+"\n");
				last = i+1;
			}
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

	public static String mark(String rLine, int index){
			//return a carrot pointing to the different character in the line
			String mark = " ";
			for(int i=0; i<rLine.length(); i++){
				if(i == index){
					mark += "^";
				}
				else{
					mark += " ";	
				}
			}
			return mark;
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
	//text color
	String RESET = "\u001B[0m";
	String BLACK = "\u001B[30m";
	String RED = "\u001B[31m";
	String GREEN = "\u001B[32m";
	String YELLOW = "\u001B[33m";
	String BLUE = "\u001B[34m";
	String PURPLE = "\u001B[35m";
	String CYAN = "\u001B[36m";
	String WHITE = "\u001B[37m";
	//background color
	String BLACK_BACKGROUND = "\u001B[40m";
	String RED_BACKGROUND = "\u001B[41m";
	String GREEN_BACKGROUND = "\u001B[42m";
	String YELLOW_BACKGROUND = "\u001B[43m";
	String BLUE_BACKGROUND = "\u001B[44m";
	String PURPLE_BACKGROUND = "\u001B[45m";
	String CYAN_BACKGROUND = "\u001B[46m";
	String WHITE_BACKGROUND = "\u001B[47m";

	String highlight = BLUE_BACKGROUND+RED+line.substring(0,index);
	highlight += BLACK_BACKGROUND+WHITE + rdiff + BLUE_BACKGROUND+RED;
	highlight += line.substring(index + rdiff.length(),line.length())+RESET;
	return highlight;
	}

	public static String difference(String result, String correct) {
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
			context[2] = "       "+mark(rList.get(line),index);
			if(line < (rList.size()-1)){
				context[3] = "Line "+(line+1)+": "+rList.get(line+1);
			}
			for(String in: context){
				message += in+"\n";
			}
		}
		else{
			message = "";
		}
		return message;
	}

	public static void main(String[] args){
		String correct = "line 1\nline 2\nline 3\nline 4\nHello World!\nanother\nline";
		String result = "line 1\nline 2\nline 3\nline 4\nHello WOrld\nanother\nline";
		System.out.println(difference(result, correct));
	}
}

