# https://stackoverflow.com/questions/7016249/compiling-java-from-python

import subprocess
PIPE = subprocess.PIPE
def compile_java(java_file):
	'''compile java program, if output it failed'''
	cmd = 'javac ' + java_file
	proc = subprocess.Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
	out = proc.communicate()
	if out[0] or out[1]:
		return False #compile failed - there was output
	else:
		return True

def run_java(java_class):
	'''run a compiled java program and caputre output, must be in the same dir as the file'''
	cmd = "java " + java_class
	proc = subprocess.Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
	out, err = proc.communicate()
	if err:
		print(err.decode())
	return out.decode()

def git_log():
	'''get the timestamp of the latest commit'''
	cmd = "git log -1 --format=%ci"
	p = subprocess.Popen(cmd,shell=True,stdout=PIPE,stderr=PIPE)
	out,err = p.communicate()
	if err:
		print(err.decode())
	return out.decode()
