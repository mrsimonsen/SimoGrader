public class Diff{
	public static String difference(String result, String correct) {
		int i;
		int at = -1;//index of the different character in the whole string
		int line = 0;//number of lines
		int index = 0;//index of different character in the line
		String message = "";//helpful display message for students
		String diffc = "";//what the character was supposed to be
		String diffr = "";//what the character was
		String surroundings = "";//a line before or a line after (or both) to give context
			

		//iterate through the strings
		for (i = 0; i < result.length() && i < correct.length(); i++) {
			//count the nuber of lines in the correct string
			if (correct.charAt(i)=='\n'){
				line++;
			}
			//stop if the characters don't match
			if (result.charAt(i) != correct.charAt(i)) {
				break;
			}
		}
		//where we broke is where the strings were different
		if (i < result.length() || i < correct.length()) {
			at = i;
		}
		//if the strings were different
		if (at >= 0) {
			//display escape sequence if it's a whitespace character
			if (Character.isWhitespace(correct.charAt(at))){
				switch (correct.charAt(at)){
					case '\t':
						diffc = "\\t";
						break;
					case '\n':
						diffc = "\\n";
						break;
					case '\r':
						diffc = "\\r";
						break;
					default:
						diffc = " ";
						break;
				}
			}
			else{//not a whitespace character
				diffc += correct.charAt(at);
			}
			//do the same for the result
			if (Character.isWhitespace(result.charAt(at))){
				switch (result.charAt(at)){
					case '\t':
						diffr = "\\t";
						break;
					case '\n':
						diffr = "\\n";
						break;
					case '\r':
						diffr = "\\r";
						break;
					default:
						diffr = " ";
						break;
				}
			}
			else{
				diffr += correct.charAt(at);
			}
			//find the index on the line


				//make the message
				message += "Expected '"+diffc+"', but was '"+diffr+"'\n";
				message += "On line "+line+", index "+index"
				message += "\nReference to difference from ";
				if (at > correct.length()/2){
					rest = "ending: "+result.substring(at);
				}
				else{
					rest = "beginning: "+result.substring(0,at+1);
				}
				message+=rest;
			}
			return message;
	}

	public static void main(String[] args){
		String correct = "line 1\nline 2\nline 3\nline 4\nHello World!";
		String result = "line 1\nline 2\nline 3\nline 4\nHello\tWOrld";
		System.out.println(difference(result, correct));
	}
}
