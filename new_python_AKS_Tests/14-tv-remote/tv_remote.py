#Mr. Simonsen
#14

class Remote():

	def __init__(self):
		self.__channel = 3
		self.__volume = 5
		
	def __str__(self):
		rep = f"Channel: {self.__channel}\n"
		rep += f"Volume: {self.__volume}"
		return rep
	
	@property
	def channel(self):
		return self.__channel
	
	@channel.setter
	def channel(self, new):
		if 1 <= new <= 100:
			self.__channel = new
		else:
			print(f"'{new}' is out of the channel range")
		
	def volume_up(self):
		self.__volume += 1
		if self.__volume > 10:
			self.__volume = 10
	
	def volume_down(self):
		self.__volume -= 1
		if self.__volume < 0:
			self.__volume = 0
	
	def channel_up(self):
		self.__channel += 1
		if self.__channel > 100:
			self.__channel = 1
	
	def channel_down(self):
		self.__channel -= 1
		if self.channel < 1:
			self.__channel = 100
	
	def set_channel(self, new):
		try:
			x = int(new)
			self.channel = x
		except ValueError as e:
			print(f"Error: {e}")
			print(f"Explanation: '{new}' isn't a number")
	
	
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