# Instructions
Project 8, extend assignment 15

## Steps
1. This project extends assignment 15, so you're going to want to have that assignment handy. Also, you've been given the main function for this program; it should not be modified.
2. Create the parse_data() function, which takes a data string, and a dictionary as parameters, but returns nothing. Modify your code from assignment 15 so that it does the following:
	* Tries to convert the second part of the data string to an integer. If it can't it should display:
	``Error: Comma not followed by an integer.``
	* If the conditions mentioned above and the conditions from assignment 15 are met, create a new entry in the given dictionary where the key is the data string, and the value is the integer value.
	* Change the success output to match the example output.
3. Create the output_table() function. This function has 4 parameters: a dictionary, a title, a column1 header, and a column2 header. This function returns nothing.
	* Display a newline plus the title right justified to 33 characters.
	* Display the column headers on the same line, separated by a vertical line.
	* The first column header should be justified left justified to 20 characters, the second column header right justified to 23 characters.
	* Print out a line of hyphens that is 44 characters long.
	* For each key in the dictionary, display the key, left justified to 20 characters, a vertical line, then the value of that key right justified to 24 characters.
4. Create the output_histogram function, which has a single parameter of a dictionary and returns nothing.
	* For each key in the dictionary, display the key right justified 20 characters, followed by a space, the a number of asterisks equal the the value that's stored in that key.

The output of the program should look like the following:
```
Enter a title for the data:
Number of Novels Authored
Enter the column 1 header:
Author name
Enter the column 2 header:
Number of novels
Enter a data point ('done' to stop input):
Jane Austen,6
Data string: Jane Austen
Data integer: 6
Enter a data point ('done' to stop input):
Charles Dickens,20
Data string: Charles Dickens
Data integer: 20
Enter a data point ('done' to stop input):
Ernest Hemingway 9
Error: No comma in string.
Enter a data point ('done' to stop input):
Ernest hemingway9
Error: No comma in string.
Enter a data point ('done' to stop input):
Ernest Hemingway,9
Data string: Ernest Hemingway
Data integer: 9
Enter a data point ('done' to stop input):
Jack Kerouac,22
Data string: Jack Kerouac
Data integer: 22
Enter a data point ('done' to stop input):
F, Scott Fitzgerald,8
Error: Too many commas in string.
Enter a data point ('done' to stop input):
F. Scott, Fitzgerald, 8    
Error: Too many commas in string.
Enter a data point ('done' to stop input):
F.   Scott   Fitzgerald,   8  
Data string: F. Scott Fitzgerald
Data integer: 8
Enter a data point ('done' to stop input):
Mary Shelley, 7
Data string: Mary Shelley
Data integer: 7
Enter a data point ('done' to stop input):
Charlotte Bronte, 5
Data string: Charlotte Bronte
Data integer: 5
Enter a data point ('done' to stop input):
Mark Twain, 11
Data string: Mark Twain
Data integer: 11
Enter a data point ('done' to stop input):
Agatha Christie,seventythree
Error: Comma not followed by an integer.
Enter a data point ('done' to stop input):
Agatha Christie,70three
Error: Comma not followed by an integer.
Enter a data point ('done' to stop input):
Agatha Christie,seventy3
Error: Comma not followed by an integer.
Enter a data point ('done' to stop input):
Agatha Christie, 73
Data string: Agatha Christie
Data integer: 73
Enter a data point ('done' to stop input):
Ian Fleming,14
Data string: Ian Fleming
Data integer: 14
Enter a data point ('done' to stop input):
J.K. Rowling,14
Data string: J.K. Rowling
Data integer: 14
Enter a data point ('done' to stop input):
Stephen King,    54
Data string: Stephen King
Data integer: 54
Enter a data point ('done' to stop input):
Oscar Wilde,1
Data string: Oscar Wilde
Data integer: 1
Enter a data point ('done' to stop input):
done
        Number of Novels Authored
Author name         |       Number of novels
--------------------------------------------
Jane Austen         |                      6
Charles Dickens     |                     20
Ernest Hemingway    |                      9
Jack Kerouac        |                     22
F. Scott Fitzgerald |                      8
Mary Shelley        |                      7
Charlotte Bronte    |                      5
Mark Twain          |                     11
Agatha Christie     |                     73
Ian Fleming         |                     14
J.K. Rowling        |                     14
Stephen King        |                     54
Oscar Wilde         |                      1
         Jane Austen ******
     Charles Dickens ********************
    Ernest Hemingway *********
        Jack Kerouac **********************
 F. Scott Fitzgerald ********
        Mary Shelley *******
    Charlotte Bronte *****
          Mark Twain ***********
     Agatha Christie *************************************************************************
         Ian Fleming **************
        J.K. Rowling **************
        Stephen King ******************************************************
         Oscar Wilde *
```
*Note: This program outputs a newline after each input and the example show the user's input, but that actually isn't part of the output when the program runs.*