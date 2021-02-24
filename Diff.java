import java.util.ArrayList;

public class Diff{
	public static ArrayList<String> splitter (String thing){
		ArrayList<String> list = new ArrayList<String>();
		int last = 0;
		for (int i=0; i<thing.length();i++){
			if(thing.charAt(i) == '\n'){
				list.add(thing.substring(last, i));
				last = i;
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

	public static String getChar(char thing){
		//display escape sequence if it's a whitespace character
		if (Character.isWhitespace(thing)){//check the correct character
			switch (thing){
				case '\t':
					return "\\t"; 
				case '\n':
					return "\\n";
				case '\r':
					return "\\r";
			}
		}
		else{
			return ""+thing;
		}
	}

	public static String mark(String rLine, int index){
			//return a carrot pointing to the different character in the line
			String mark = "";
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

	public static String difference(String result, String correct) {
		int line;//line number
		int index;//index of different character in the line
		String message = "";//helpful display message for students
		String cdiff = "";//what the character was supposed to be
		String rdiff = "";//what the character was

		//split both strings into arrays at \n
		ArrayList<String> rList = splitter(result);
		ArrayList<String> cList = splitter(correct);

		//find the line and index number of the first difference
		int[] temp = locate(rList,cList);
		line = temp[0];
		index = temp[1];
		
		//if the strings were different
		if (index >= 0 && line >= 0) {
			//get the different characters
			cdiff = getChar(cList[line].charAt(index));
			rchar = getChar(rList[line].charAt(index));
				
			String[] context = {"","","",""};
			if(line > 0){
				context[0] ="Line "+(line-1)+":" +"\t"+ rList[line-1];
			}
			context[1] = "Line "+(line)+":"+"\t"+rList[line];
			context[2] = "       "+mark(rLine[line],index);
			if(line < (rList.length-1)){
				context[3] = "Line "+(line+1)+":"+"\t"+rList[line+1];
			}

			//TODO: Add color - https://stackoverflow.com/questions/5762491/how-to-print-color-in-console-using-system-out-println
			//make the message
			message += "Expected '"+cdiff+"', but was '"+rdiff+"'\n";
			message += "On line "+line+", index "+index+"\n";
			message += "Context:\n";
			for(String in: context){
				message += in+"\n";
			}
		}
		else{
			message = "";
		*/
		return message;
	}

	public static void main(String[] args){
		String correct = "line 1\nline 2\nline 3\nline 4\nHello World!\nanother\nline";
		String result = "line 1\nline 2\nline 3\nline 4 Hello WOrld\nanother\nline";
		System.out.println(difference(result, correct));
	}
}

