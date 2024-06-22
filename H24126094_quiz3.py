print("Welcome to the simple calculator program!")
#歡迎訊息

want = "yes"
#意願

while want == "yes":
	num1 = int(input("Enter the first number: "))
	num2 = int(input("Enter the second number: "))
	operation = str(input("Select an arithmetic operation (+, -, *, /): "))
	#每次計算前都要問的問題
	while want == "yes":
		if operation == "+":
			result = float(num1 + num2)
			print("Result: " , result)
			break
		elif operation == "-":
			result = float(num1 - num2)
			print("Result: " , result)
			break
		elif operation == "*":
			result = float(num1 * num2)
			print("Result: " , result)
			break
		else:
			if num2 == 0:
				print("Error: Division by zero!")
				break
				#當分母是0，直接離開這個迴圈，回到問數字和加減乘除
			else:
				result = float(num1 / num2)
				print("Result:", result)
				break
	#計算機
	want = str(input("Do you want to perform another calculation? (yes or no):"))
	#詢問意願
print("Goodbye!")
#離開訊息
