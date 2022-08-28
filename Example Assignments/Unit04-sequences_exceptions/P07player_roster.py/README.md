# Instructions
Project 7

## Steps
1. Prompt the user for 5 jersey numbers and ratings - save them into a two-dimensional list where each element represents a player [jersey, rating]. Then display the roster check the example output for formatting.
2. Display the menu and prompt for user input. Loop this until the user input is 'q'.
3. Implement the "Output roster" menu option. This should display the current values from the 2D list.
4. Implement the "Output players above a rating" menu option. Note that this is above a rating, not above or equal to a rating. If there are no players above the entered rating, still display the title. Check the example output for formatting.
5. Implement the "Update player rating" menu option. This should ask for a jersey number and new rating regardless of the jersey number existing in the roster list. Check the example output for formatting.
6. Implement the "Replace player" menu option. This should ask for a jersey number and only ask for a new jersey and rating if the first jersey is in the roster.  Check the example output for formatting.


The output of the program should look like the following:
```
Enter player 1's jersey number:
84
Enter player 1's rating:
7

Enter player 2's jersey number:
23
Enter player 2's rating:
4

Enter player 3's jersey number:
4
Enter player 3's rating:
5

Enter player 4's jersey number:
30
Enter player 4's rating:
2

Enter player 5's jersey number:
66
Enter player 5's rating:
9

ROSTER
Player 1 -- Jersey number: 84, Rating: 7
Player 2 -- Jersey number: 23, Rating: 4
Player 3 -- Jersey number: 4, Rating: 5
Player 4 -- Jersey number: 30, Rating: 2
Player 5 -- Jersey number: 66, Rating: 9

MENU
u - Update player rating
a - Output players above a rating
r - Replace player
o - Output roster
q - Quit

Choose an option:
u
Enter a jersey number:
30
Enter a new rating for player:
10

MENU
u - Update player rating
a - Output players above a rating
r - Replace player
o - Output roster
q - Quit

Choose an option:
r
Enter a jersey number:
10

MENU
u - Update player rating
a - Output players above a rating
r - Replace player
o - Output roster
q - Quit

Choose an option:
r
Enter a jersey number:
4
Enter a new jersey number:
14
Enter a rating for the new player:
1

MENU
u - Update player rating
a - Output players above a rating
r - Replace player
o - Output roster
q - Quit

Choose an option:
a
Enter a rating:
4

ABOVE 4
Player 1 -- Jersey number: 84, Rating: 7
Player 4 -- Jersey number: 30, Rating: 10
Player 5 -- Jersey number: 66, Rating: 9


MENU
u - Update player rating
a - Output players above a rating
r - Replace player
o - Output roster
q - Quit

Choose an option:
o
ROSTER
Player 1 -- Jersey number: 84, Rating: 7
Player 2 -- Jersey number: 23, Rating: 4
Player 3 -- Jersey number: 14, Rating: 1
Player 4 -- Jersey number: 30, Rating: 10
Player 5 -- Jersey number: 66, Rating: 9

MENU
u - Update player rating
a - Output players above a rating
r - Replace player
o - Output roster
q - Quit

Choose an option:
q
```
*Note: This program outputs a newline after each input and the example show the user's input, but that actually isn't part of the output when the program runs.*
