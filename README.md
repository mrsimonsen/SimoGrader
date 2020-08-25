# AutoGrader
Autograder and testing files for CS 1030 (python), CS 1400 (Java), and CS 1410 (C++)

Made for Ubuntu for Windows

## TOC
* simogit.py
	* Python3 script that will clone all repositories defined in the .env file.
* .env
	* Contains details for the program to access GitHub, and the prefix of repos to clone.
* setup.sh
	* Sets up a Linux machine (empty CodeAnywhere container) with Python, Java, and C++
* grade.sh
	* Runs simogit then autograde. Removes the cloned repos when finished.

## Notes
* Edit .env file to match class you're wanting to grade
* Edit grade.sh file to match assignment you're wanting to grade
* input() needs to have a new line in the string so that the tests match the output - https://stackoverflow.com/questions/33984941/how-to-make-pythons-subprocess-interact-with-input
