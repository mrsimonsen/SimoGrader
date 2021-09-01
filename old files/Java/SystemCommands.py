# https://stackoverflow.com/questions/7016249/compiling-java-from-python
from subprocess import run

def compile_java(java_file):
	'''compile java program, if output it failed'''
	p = run(f'javac {java_file}', shell=True, capture_output=True)
	if p.stdout or p.stderr:
		return False #compile failed - there was output
	else:
		return True

def run_java(java_class):
	'''run a compiled java program and caputre output, must be in the same dir as the file'''
	p = run(f'java {java_class}', shell=True, capture_output=True, text=True)
	if e := p.stderr:
		print(e)
	return p.stdout

def git_log():
	'''get the timestamp of the latest commit'''
	p = run(f'git log -1 --format=%ci',shell=True,capture_output=True, text=True)
	if e := p.stderr:
		print(e)
	return p.stdout
