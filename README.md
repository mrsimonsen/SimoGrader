# AutoGrader
Autograder and testing files for CS 1030 (python), CS 1400 (Java), and CS 1410 (C++)

Made for Ubuntu for Windows

## Setup
* cp .vimrc ../.
* edit .bashrc and add the following to the end of the file:
```
alias all="python3 all.py"
```
* .env
	* Must be created with the contents of
	```TOKEN=your_token
	```
	where your_token is replaced with a GitHub Personal Access Token.
* sudo apt install python3-pip default-jdk
* pip3 install pygithub
* pip3 install python-dotenv
* [install GitHub CLI](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)
	* use ssh
* Setup a new [SSH key](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/connecting-to-github-with-ssh) and link to account 
##TOC

## Notes
* Edit .env file to match class you're wanting to grade
* Edit grade.sh file to match assignment you're wanting to grade
* input() needs to have a new line in the string so that the tests match the output - https://stackoverflow.com/questions/33984941/how-to-make-pythons-subprocess-interact-with-input
