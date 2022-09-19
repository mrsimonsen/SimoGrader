def main():
	title = input("Enter a title for the data:\n")
	col1 = input("Enter the column 1 header:\n")
	col2 = input("Enter the column 2 header:\n")
	data_points = {}
	data = 'a'
	while data != 'done':
		data = input("Enter a data point ('done' to stop input):\n")
		parse_data(data, data_points)
	output_table(data_points, title, col1, col2)
	output_histogram(data_points)