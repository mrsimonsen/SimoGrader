# Example Assignments
I have the assignments broken into units, plus an interim assignment for right after winter break to get students back on track.

Every assignment should start as a template(link to instructions on how to make a repo a template) repository that students gain access to through GitHub Classroom link (link to instructions on making a github classroom).

Every assignment template repo should have the file structure:
- [.github folder](#.github-folder)
	- classroom folder
		- [autograding.json](#classroom/autograding.json)
	- workflows folder
		- [classroom.yml](#workflows/classroom.yml)
- [.gitattributes](#.gitattributes)
- [.gitignore](#.gitignore)
- [README.md](#readme.md)
- [tests.py](#tests.py)
- [student.py](#student.py)

## .github folder
This hidden folder contains the files that cause GitHub Actions to run the test.py file automatically on a pull request. The contents of this folder must be identical across all assignments template repositories.
### classroom/autograding.json
This file lets GitHub Actions know where the tests are located. If you don't call your testing file "tests.py", you'll need to update line 6 to match.
### workflows/classroom.yml
This file sets up the GitHub Actions hook to run the autograding.json commands. You can set a different hook to change when the tests run on GitHub on line 3 (like 'push' to run every push).

## .gitattributes
I suggest having a gitattributes to preform end of line normalization. This way the tests and student code (regardless of the OS they're working on) will have the same line endings. I have it set to lf since my classroom is running on linux-based OS. If you're working primarily with Windows you may want to change this to crlf. *NOTE: Make sure your line endings match what you're looking for in your tests.*

## .gitignore
This files tells git what files or folders to ignore from the version control. Running tests creates a "\_\_pycache\_\_" folder that we don't want to keep in version control. I also have the README.md and tests.py file ignored so that if students *accidentally* make a change to those files they wont be pushed to GitHub. So GitHub actions will let them know that they're not passing the tests even if they edited them on their local machine.

My examples call this file "ignore.txt", so as to not make this repo drop the listed files. *NOTE: you should add the README.md and tests.py file to GitHub **BEFORE** creating the .gitignore file (or renaming the ignore.txt file to that name).*

## README.md
GitHub will automatically display this file when named this way. I use the README for the assignment's instructions.

## tests.py
This file contains the tests for the current assignment. If you choose to go with a different name for your test file, be sure to update the autograding.json file to match. Also, notice that the student's copy of the tests is not the copy the autograder uses to do the actual grading, this helps prevent cheating.

## student.py
For simplicity, I have every assignment's main file called the same thing; made writing the autograder much easier. Assignments can have more than one file that students need to work on, but those will be imported into student.py.