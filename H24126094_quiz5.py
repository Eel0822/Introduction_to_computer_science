#H24126094 統計116 李繕安
size = int(input("Enter the size of the grid: "))
done = False

#建立棋盤
for i in range(0,size-1):
    for j in range(0,size):
        print("_",end=" ")
    print("\n")
print("_ "*size)

#要求使用者輸入要替換的位置和字符
while done == False:
    co = str(input("Enter the cell coordinate to edit: "))
    #當使用者輸入done，表示結束
    if co == "done":
        break
    cell = str(input("Enter the new value for the cell: "))
    co_split = co.split(",")
    co_split_1 = int(co_split[0])
    co_split_2 = int(co_split[1])