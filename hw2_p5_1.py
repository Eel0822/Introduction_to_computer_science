number=int(input("Input an integer number: "))
a,b=0,1
i=0
while i<number-1:
	a,b=b,a+b 
	i+=1
str(number)
print("The %s-th Fibonacci sequence number is:"%(number),b)
