#統計116 H24126094 李繕安
i, j = 9, 9 #設定初始值
while i > 0: #設定迴圈的條件
    while j > 0: #設定迴圈的條件
    	#print乘法表
        print(j, "x", i, "=", j*i, end="\t")
        print(j, "x", i-1, "=", j*(i-1), end="\t")
        print(j, "x", i-2, "=", j*(i-2))
        j -= 1 #乘數-1
    print() #區間段的空格
    i -= 3 #被乘數-3
    j = 9 #重新設定i=9

