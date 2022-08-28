# Instructions
Project 4

## Steps
1. Display the intro.
2. Get an integer month, day and year from the user.
3. Using the equation below, calculate the weekday of the entered date and display it. 0 is Sunday.

**Before using the equation below**<br>*January and February entries need to have 12 added to the month and 1 subtracted from the year*
![zellers congruence equation for computers](https://latex.codecogs.com/svg.image?%5Cmathrm%7B%5Cleft%20%5Clfloor%20represents%5C%20integer%5C%20division%20%5Cright%20%5Crfloor%7D%5C%5C%20%5Cmathrm%7B%25%5C%20represents%5C%20modulus%5C%20division%7D%5C%5Cday%5C_of%5C_week%20=%20%5Cleft%20(%20day%20&plus;%5Cleft%20%5Clfloor%20%5Cbegin%7Bmatrix%7D%5Cunderline%7B31(month-2)%7D%20%5C%5C%2012%5Cend%7Bmatrix%7D%5Cright%20%5Crfloor%20&plus;%20year%20&plus;%5Cleft%20%5Clfloor%20%5Cbegin%7Bmatrix%7D%5Cunderline%7Byear%7D%20%5C%5C%204%5Cend%7Bmatrix%7D%5Cright%20%5Crfloor-%5Cleft%20%5Clfloor%20%5Cbegin%7Bmatrix%7D%5Cunderline%7Byear%7D%20%5C%5C%20100%5Cend%7Bmatrix%7D%5Cright%20%5Crfloor&plus;%5Cleft%20%5Clfloor%20%5Cbegin%7Bmatrix%7D%5Cunderline%7Byear%7D%20%5C%5C%20400%5Cend%7Bmatrix%7D%5Cright%20%5Crfloor%20%5Cright%20)%20%25%207)
The output of the program should look like the following:
```
Enter a date and I'll tell you what weekday it was/is/will be.
Enter a month (1-12):
3
Enter a day (1-31):
1
Enter a year (YYYY):
1988

Tuesday
```
*Note: This program outputs a newline after each input and the example show the user's input, but that actually isn't part of the output when the program runs.*
