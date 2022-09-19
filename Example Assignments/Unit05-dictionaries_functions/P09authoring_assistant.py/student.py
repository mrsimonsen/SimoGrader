def main():
	data = input("Enter sample text:\n")
	choice = None
	while choice != 0:
		choice = print_menu(data)

		if choice == 1:
			data = replace_exclamation(data)
			print(f"Edited text: {data}")
		elif choice == 2:
			data = shorten_space(data)
			print(f"Edited text: {data}")
		elif choice == 3:
			print(f"Number of non-whitespace characters: {num_non_ws(data)}")
		elif choice == 4:
			print(f"Number of words: {num_words(data)}")
		elif choice == 5:
			find = input("Enter a word or pharase to be found:\n")
			print(f'"{find}" instances: {find_text(find, data)}')