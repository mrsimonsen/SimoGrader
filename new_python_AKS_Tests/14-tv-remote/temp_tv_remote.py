#Name
#Period

def main():
	r = Remote()
	print(r)
	user = ''
	MENU = '''
vu - Volume Up
vd - Volume Down
cu - Channel Up
cd - Channel Down
set - Set Channel
q - Quit
'''
	while user != 'q':
		print(MENU)
		user = input("Select an option:\n")
		if user == 'vu':
			r.volume_up()
		elif user == 'vd':
			r.volume_down()
		elif user == 'cu':
			r.channel_up()
		elif user == 'cd':
			r.channel_down()
		elif user == 'set':
			r.set_channel(input("What channel?\n"))
		elif user == 'v':
			print(r)
		elif user == 'q':
			print("Goodbye.")
		else:
			print(f"{user} is not a valid option")

if __name__ == '__main__':
	main()