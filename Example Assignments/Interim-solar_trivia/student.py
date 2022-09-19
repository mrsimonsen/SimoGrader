import datetime

def main():
	#set today's date and earth's orbit
	today = datetime.date.today()
	Earth_orbit = 365.25

	#TODO: code part 1 here
	###############

	#set birthday date
	birthday = datetime.date(year, month, day)
	#calculate number of days on earth
	earth_days = (today - birthday).days
	#calculate age, rounded to 1 decimal place
	earth_age = round(earth_days/Earth_orbit,1)

	#TODO: complete the data table with values relative to Earth
	#(planet name,orbit period,gravity,rotational period)
	data = (
		('Mercury', 0, 0, 0),
		('Venus', 0, 0, 0),
		('Earth', 1, 1, 1),
		('Mars', 0, 0, 0),
		('Jupiter', 0, 0, 0),
		('Saturn', 0, 0, 0),
		('Uranus', 0, 0, 0),
		('Neptune', 0, 0, 0)
	)
	###############

	print(f"\nSolar System data for {name}")
	#create row strings
	row1 = "Planet |"
	row2 = "Age    |"
	row3 = "Weight |"
	row4 = "Days   |"

	#for each planet in the data table
	for entry in data:
		#unpack values
		planet, orbit, gravity, rotation = entry
		#TODO: calculate age on this planet, rounded to 1 decimal place
		#TODO: calculate weight on this planet, rounded to 2 decimal places
		#TODO: calculate number of days for this planet, rounding down to the nearest integer
		#append values to row strings
		row1 += f"{planet:7}|"
		row2 += f"{age:7}|"
		row3 += f"{weight:7}|"
		row4 += f"{days:7}|"

	#display table rows
	print(row1)
	print(row2)
	print(row3)
	print(row4)

if __name__ == "__main__":
	main()