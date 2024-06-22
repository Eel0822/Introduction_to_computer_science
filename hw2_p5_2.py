string = input("Enter a string: ")
right = len(string) - 1

def isPalindrome(string):
	left = 0
	right = len(string) - 1
	while right > left:
		if string[left] != string[right]:
			return False
		left += 1
		right -= 1
	return True

maxstring = ""
maxlength = 0

for i in range (0 , right+1):
	for j in range (i+1 , right+1):
			if ( j-i < maxlength):
				break
			elif string[i] == string[j]:
				if isPalindrome(string[i:j+1]):
					length = j - i + 1
					if (length > maxlength):
						maxlength = length
						maxstring = string[i:j+1]

print("Longest palindrome substring is:" , maxstring)
print("Length is:" , maxlength)