# Instructions
Project 2

## Steps
1. Prompt the user for the length of a cube in inches and store it as an integer.
2. Calculate and display the volume of the cube.
3. Calculate and display the diameter of a sphere that has the same volume. See the equation below, you'll need to do some algebra.
4. Calculate and display the diameter of circumscribed sphere for that cube. See equations below, it gives you the radius.
5. Calculate and display the weight of that volume in the metals of the table below. You'll need to calculate the density for the alloys listed. Format each line so that the metal name is left justified to a minimum of 10 characters. Format the density to always display 2 decimal places.

![circumscribed sphere equation](https://latex.codecogs.com/svg.image?%5Cmathrm%7BCurcumscribed%5C%20sphere%5C%20of%5C%20cube%7D:%20%5Cbegin%7Bmatrix%7D%5Cunderline%7B%5Csqrt%7B3%7D%7D%20%5C%5C%202%5Cend%7Bmatrix%7D%20%5Ctimes%20edge)

![sphere volume equation](https://latex.codecogs.com/svg.image?%5Cmathrm%7BVolume%5C%20of%5C%20a%5C%20sphere:%5Cbegin%7Bmatrix%7D%5Cunderline%7B4%7D%20%5C%5C%203%5Cend%7Bmatrix%7D%20%5Ctimes%20%5CPi%20%5Ctimes%20radius%5E%7B3%7D)

Metal | Density (lb/in3)
-- | --
Al | 0.098
Cu | 0.324
Ag | 0.379
Au | 0.698

Alloy | Composition
--|--
Bronze-Al | 95% Cu<br>5% Al
Rose Gold | 75% Au<br>20% Cu<br>5% Ag

The output of the program should look like the following:
```
Input a side of a cube (in inches):
5
The cube's volume is 125 in^3.
A sphere with the same volume has a diameter of 6.20 inches.
The cube would fit in a sphere with a diameter of 8.66 inches.
The weight of that volume in various metals:
Aluminum  = 12.25 lbs
Bronze-Al = 39.09 lbs
Copper    = 40.50 lbs
Silver    = 47.38 lbs
Rose Gold = 75.91 lbs
Gold      = 87.25 lbs
```
*Note: This program outputs a newline after each input and the example show the user's input, but that actually isn't part of the output when the program runs.*
