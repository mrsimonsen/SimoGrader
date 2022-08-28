# Simonsen Auto-Grader

I originally created this terminal program to collect student assignments hosted on GitHub then test/grade them and store the results in a database to enter into my school's SIS, but all privately to protect student information and keep my assignments and tests private.

I'm now making a public repo to show off my work with example data so that other's can benefit from my years of work. This will be a work in progress, and progress can be tracked through the TODO list below.

TODOs
- [ ] Choose or make a public license before moving to public reo
- [ ] Purge student data before making public repo
- [ ] modify database to no longer include assignment list, instead scan Testing folder for assignment prefixes.
- [ ] Create Example Assignments folder (copy templates without AKs)
- [ ] docs folder for all Instruction .md files
- [ ] GUI using TKinter?
- [ ] shelve to sqlite3 -> allowing custom queries and reports

Instructions to make
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
