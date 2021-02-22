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
		int[] locations = {0,0};//line, index
		int line = -1;
		int index = 0;

		return locations;
	}

	public static String difference(String result, String correct) {
		int line;//line number
		int index;//index of different character in the line
		String message = "";//helpful display message for students
		String cdiff = "";//what the character was supposed to be
		String rdiff = "";//what the character was
		char cchar;
		char rchar;
		int i;

		//split both strings into arrays at \n
		ArrayList<String> rList = splitter(result);
		ArrayList<String> cList = splitter(correct);

		//iterate through the list of strings
		boolean notFound = true;
		

		//iterate through the list of strings
		while (notFound){
			line++;
			for(index = 0; index < rList.get(line).length() && index < cList.get(line).length();index++){
				//stop if the characters don't match
				if (rList.get(line).charAt(index) != cList.get(line).charAt(index)) {
					notFound = false;
					break;
				}
			}
			notFound = false;
		}
		
		/*//if the strings were different
		if (index >= 0 && line >= 0) {
			//get the different characters
			cchar = cList[line].charAt(index);
			rchar = rList[line].charAt(index);

			//display escape sequence if it's a whitespace character
			if (Character.isWhitespace(cchar)){//check the correct character
				switch (cchar){
					case '\t':
						cdiff = "\\t";
						break;
					case '\n':
						cdiff = "\\n";
						break;
					case '\r':
						cdiff = "\\r";
						break;
				}
			}
			else{
				cdiff += cchar;
			}
			if (Character.isWhitespace(rchar)){
				switch (rchar){//check the result character
					case '\t':
						rdiff = "\\t";
						break;
					case '\n':
						rdiff = "\\n";
						break;
					case '\r':
						rdiff = "\\r";
						break;
				}
			}
			else{
				rdiff += rchar;
			}
		
			String mark = "";
			for(i=0; i<rList[line].length();i++){
				if(i == index){
					mark += "^";
				}
				else{
					mark += " ";
				}
			}
				
			String[] context = {"","","",""};
			if(line > 0){
				context[0] ="Line "+(line-1)+":" +"\t"+ rList[line-1];
			}
			context[1] = "Line "+(line)+":"+"\t"+rList[line];
			context[2] = "\t"+mark;
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
		//System.out.println(difference(result, correct));
		System.out.println(splitter(correct));
	}
}

