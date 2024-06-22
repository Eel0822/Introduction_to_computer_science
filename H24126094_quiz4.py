#H2416094 統計116 李繕安

#輸入要尋找的資料
aim = str(input("Enter a sequence of integers seperate by white space: "))
#建立兩個空串列
LICS_1 = []
LICS_2 = []
#用空白格區分辨建立串列
aim_list = aim.split(" ")
now = int(aim_list[0])
length_1 = 1
length_2 = 1
largest = int(aim_list[0])

#比較要尋找的資料
for i in aim_list:
	#如果數字比前面的大，長度增加一
    if int(i) > largest:
        largest = int(i)
        LICS_1.append(i)
        length_1 += 1
    #如果數字比前面的小，重新開啟一個比較
    elif int(i) <= largest:
        largest = int(i)
        if int(i) > largest:
            largest = int(i)
            LICS_2.append(i)
            length_2 += 1

if length_1 > length_2:
    print(length_1)
else:
    print(length_2)