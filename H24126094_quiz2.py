shopping=int(input("Enter the shopping amount: "))
level=str(input("Enter the membership level (Regular or Gold): "))
if level=="Regular":
	if shopping<=1000:
		shopping=shopping
		print("Regular",shopping)
	elif 1000<shopping<=2000:
		shopping=shopping*0.9
		print("Regular",shopping)
	elif 2000<shopping<=3000:
		shopping=shopping*0.85
		print("Regular",shopping)
	else:
		shopping=shopping*0.8
		print("Regular",shopping)
elif level=="Gold":
	if shopping<=1000:
		shopping=shopping
		print("Gold",shopping)
	elif 1000<shopping<=2000:
		shopping=shopping*0.85
		print("Gold",shopping)
	elif 2000<shopping<=3000:
		shopping=shopping*0.8
		print("Gold",shopping)
	else:
		shopping=shopping*0.75
		print("Gold",shopping)
else:
	print("Invalid member level")