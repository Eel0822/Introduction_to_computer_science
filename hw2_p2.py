#統計116 H24126094 李繕安
num=int(input("Input the range number: "))
#輸入數字
print("Perfect numbers:")
#印出Perfect numbers
for num in range(2,num+1):
#迴圈從2到輸入的數字
	numsum=sum(i for i in range(1,num) if num%i==0)
	#如果數字可以被整除，那就相加
	if numsum==num:
		print(num)
		#如果因數加總等於數字，那就印出數字
