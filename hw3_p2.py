#統計116 H24126094 李繕安
polynomial = str(input("Input polynomial: "))
x = int(input("Input the value of x: "))
polynomial_replace = polynomial.replace("+"," +").replace("-"," -1").replace("^","**").replace("X",str(x))
polynomial_split = polynomial_replace.split(" ")
result = 0
length = len(polynomial_split)
i = 0
print(polynomial_split)
for i in range(0,len(polynomial_split)):
    term = polynomial_split[i]
    if "**" in term:
        base,exp = term.split("**")
        result += int(base)**int(exp)
    elif "*" in term:
        base,exp = term.split("*")
        result += int(base)*int(exp)
    else:
        result += int(term)
    
print(polynomial_split)
print(result)