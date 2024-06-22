#統計116 H24126094 李繕安
num = int(input("Input the total number of students (n>0): "))

students = list(range(1,num+1))
index = 0

while len(students) > 1:
    for i in range (3):
        if i == 2:
            students.pop(index)
            index -= 1
        index = (index + 1) % len(students)
        
print("The last ID is :", students[0])