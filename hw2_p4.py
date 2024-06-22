#統計116 H24126094 李繕安
layer = int(input("Enter the number of layers (2 to 5) = "))
lenth_of_top = int(input("Enter the side lenth of the top layer = "))
growth = int(input("Enter the growth of each layer = "))
trunk_width = int(input("Enter the trunk width (odd number,3 to 9) = "))
trunk_height = int(input("Enter the trunk height (4 to 10) ="))

largest_height = int((lenth_of_top - 1) + growth * (layer - 1))

print(" " * (largest_height) + "#" + " " * (largest_height))
for i in range (1,layer+1):
	if i == 1:
		for a in range (1,(lenth_of_top - 1)):
			print(" " * (largest_height - a) + "#" + "@" * (2 * a - 1) + "#" + " " * (largest_height - a))
		print(" "*(growth * (layer - i)) + "#" * (2 * (largest_height - growth * (layer - i)) + 1) + " "*(growth * (layer - i)))
	elif i == 2:
		for b in range (1,(lenth_of_top - 1) + growth):
			print(" " * (largest_height - b) + "#" + "@" * (2 * b - 1) + "#" + " " * (largest_height - b))
		print(" "*(growth * (layer - i)) + "#" * (2*(largest_height - growth * (layer - i)) + 1) + " "*(growth * (layer - i)))
	elif i == 3:
		for c in range (1,(lenth_of_top - 1) + growth * 2):
			print(" " * (largest_height - c) + "#" + "@" * (2 * c - 1) + "#" + " " * (largest_height - c))
		print(" "*(growth * (layer - i)) + "#" * (2*(largest_height - growth * (layer - i)) + 1) + " "*(growth * (layer - i)))
	elif i == 4:
		for d in range (1,(lenth_of_top - 1) + growth * 3):
			print(" " * (largest_height - d) + "#" + "@" * (2 * d - 1) + "#" + " " * (largest_height - d))
		print(" "*(growth * (layer - i)) + "#" * (2*(largest_height - growth * (layer - i)) + 1) + " "*(growth * (layer - i)))
	else:
		for e in range (1,(lenth_of_top - 1) + growth * 4):
			print(" " * (largest_height - e) + "#" + "@" * (2 * d - 1) + "#" + " " * (largest_height - e))
		print(" "*(growth * (layer - i)) + "#" * (2*(largest_height - growth * (layer - i)) + 1) + " "*(growth * (layer - i)))

for n in range (1,trunk_height + 1):
	print(" " * int(largest_height - ((trunk_width - 1)/2)) + "|" * int((trunk_width - 1)/2) + "|" + "|" * int((trunk_width - 1)/2) + " " * int(largest_height - ((trunk_width - 1)/2)))

	

