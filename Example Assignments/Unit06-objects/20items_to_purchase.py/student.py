def main():
	item1 = Item()
	item2 = Item()

	print("Item 1")
	name = input("Enter the item name:\n")
	price = float(input("Enter the item price:\n"))
	quan = int(input("Enter the item quantity:\n"))
	item1.name = name
	item1.price = price
	item1.quantity = quan

	print("\nItem 2")
	item2.name = input("Enter the item name:\n")
	item2.price = float(input("Enter the item price:\n"))
	item2.quantity = int(input("Enter the item quantity:\n"))

	print("\nTOTAL COST")
	print(item1)
	print(item2)
	print(f"\nTotal: ${item1.total() + item2.total():.2f}")
################################################
#Do not change code above this line