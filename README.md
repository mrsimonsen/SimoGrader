# Simonsen Auto-Grader

I originally created this terminal program to collect student assignments hosted on GitHub then test/grade them and store the results in a database to enter into my school's SIS, but all privately to protect student information and keep my assignments and tests private.

I'm now making a public repo to show off my work with example data so that other's can benefit from my years of work. This will be a work in progress, and progress can be tracked through the TODO list below.

## Other notes
Utah strands and standards for programming 1 & 2 have changed, and now want to cover functions in the first semester and sequences (minus strings) to the second semester. I'll need to reorganize Unit 4 and 5; probably 4 with functions and string methods, and 5 with dictionaries and exceptions.

## TODOs
- [ ] Choose or make a public license before moving to public reo
- [ ] Purge student data before making public repo
- [x] modify database to no longer include assignment list, instead scan Testing folder for assignment prefixes.
- [x] Create Example Assignments folder (copy templates without AKs)
- [ ] docs folder for all Instruction .md files
- [ ] GUI using TKinter?
- [x] shelve to sqlite3 -> allowing custom queries and reports
- [ ] Drag and Drop interface for adding tests? At least a button to open the testing folder location to add test files manually.
- [ ] update .gitignore to not preserve student database.

### Instructions to make
- [ ] Each module should have detailed docstring for help()
	- [ ] database
	- [ ] student
	- [ ] tools
- [ ] setting up GitHub Classroom
	- assignment prefix for testing files
	- .github folder for automatic testing through github actions
- [ ] making assignment template repos
	- my repo structure and grader-specific files
- [ ] how to write tests
	- [ ] capture output
	- [ ] mock input
	- [ ] testing dependencies try/catch
	- [ ] test file ordering and fast-fail
- [ ] getting student data setup
	- public RSA assignment ([fireship video](https://www.youtube.com/watch?v=UFc-RPbq8kg) on automate and validate PRs) - practice git while getting student data
	- CSV import (like from a goolge form)
	- manual student entry through GUI
