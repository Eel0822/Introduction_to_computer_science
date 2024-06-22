#統計116 H24126094 李繕安
import math
year=int(input("Please input Year: "))
month=int(input("Please input Month: "))
day=0
#計算各個月的天數
if (year%4==0 and year%100!=0)or(year%400==0):
	if month in {1,3,5,7,8,10,12}:
		day=31
	elif month in {4,6,9,11}:
		day=30
	elif month in {2}:
		day=29
else:
	if month in {1,3,5,7,8,10,12}:
		day=31
	elif month in {4,6,9,11}:
		day=30
	elif month in {2}:
		day=28

#按照網路上的資料寫出每個月的一號會是星期幾
if month<=2:
	a=(year-1)//100
	b=(year-1)-(a*100)
	month=month+10
else:
	a=year//100
	b=year-(a*100)
	month=month-2

formula=((1+math.floor(2.6*month-0.2)-2*a+b+math.floor(a/4)+math.floor(b/4))%7)
if formula<0:
	formula+=7
else:
	formula=formula

#印出日曆星期
print("Sun Mon Tue Wed Thu Fri Sat")
today=1 #每個月第一天是1號
#打印出日曆
while today<=day:
	i=0
	while i<7:
		if i<formula:
			print("    ", end="")
		else:
			print("{:02}".format(today), end="  ")
			today+=1
			formula=0
			if today>day:
				break
		i+=1
	print()



