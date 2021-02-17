public class Diff{
	public static String difference(String result, String correct) {
			int at = 0;
			int i;
			String message = "";
			String diffc = "";
			String diffr = "";
			for (i = 0; i < result.length() && i < correct.length(); i++) {
					if (result.charAt(i) != correct.charAt(i)) {
							break;
					}
			}
			if (i < result.length() || i < correct.length()) {
					at = i;
			}
			if (at != 0) {
				message = "Strings differ at index "+at;
				if (Character.isWhitespace(correct.charAt(at))){
					switch (correct.charAt(at)){
						case '\t':
							diffc = "\\t";
							break;
						case '\n':
							diffc = "\\n";
							break;
						case '\f':
							diffc = "\\f";
							break;
						case '\r':
							diffc = "\\r";
							break;
						default:
							diffc = " ";
							break;
					}
				}
				else{
					diffc += correct.charAt(at);
				}
				if (Character.isWhitespace(result.charAt(at))){
					switch (result.charAt(at)){
						case '\t':
							diffr = "\\t";
							break;
						case '\n':
							diffr = "\\n";
							break;
						case '\f':
							diffr = "\\f";
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
				message += "\nExpected '"+diffc+"', but was '"+diffr+"'";
				message += "\nReference to difference from ";
				String rest;
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
		String correct = "Hello World!";
		String result = "Hello\tWOrld";
		System.out.println(difference(result, correct));
	}
}