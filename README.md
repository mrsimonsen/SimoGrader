# Simonsen Auto-Grader

*Note: GitHub CLI must be installed and configured (gh auth login) for this program to work*

I originally created this terminal program to collect student assignments hosted on GitHub then test/grade them and store the results in a database to enter into my school's SIS, but all privately to protect student information and keep my assignments and tests private.

I'm now making a public repo to show off my work with example data so that other's can benefit from my years of work. This will be a work in progress, and progress can be tracked through the TODO list below.

## TODOs
- [ ] Choose or make a public license before moving to public reo
- [X] Purge student data before making public repo
- [x] modify database to no longer include assignment list, instead scan Testing folder for assignment prefixes.
- [x] Create Example Assignments folder (copy templates without AKs)
- [x] shelve to sqlite3 -> allowing custom queries and reports
- [x] update .gitignore to not preserve student database.
- [ ] docs folder for all Instruction .md files

### Instructions to make
- [ ] Each function should have detailed docstring for help()
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
	- CSV import (like from a Google form)
