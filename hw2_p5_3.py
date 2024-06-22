number = int(input("The number of requested element in Fibonacci (n) = "))
string_1 = input("The first string for Palindromic detection (s1) = ")
string_2 = input("The second string for Palindromic detection (s2) = ")
plaintext = input("The plaintext to be encrypted: ")
right_1 = len(string_1) - 1
right_2 = len(string_2) - 1

a,b=0,1
i=0
while i<number-1:
	a,b=b,a+b 
	i+=1
str(number)

def isPalindrome_1(string_1):
	left = 0
	right = len(string_1) - 1
	while right > left:
		if string_1[left] != string_1[right]:
			return False
		left += 1
		right -= 1
	return True

def isPalindrome_2(string_2):
	left = 0
	right = len(string_2) - 1
	while right > left:
		if string_2[left] != string_2[right]:
			return False
		left += 1
		right -= 1
	return True

maxstring_1 = ""
maxlength_1 = 0
maxstring_2 = ""
maxlength_2 = 0

for i in range (0 , right_1+1):
	for j in range (i+1 , right_1+1):
			if ( j-i < maxlength_1):
				break
			elif string_1[i] == string_1[j]:
				if isPalindrome_1(string_1[i:j+1]):
					length_1 = j - i + 1
					if (length_1 > maxlength_1):
						maxlength_1 = length_1
						maxstring_1 = string_1[i:j+1]

for i in range (0 , right_2+1):
	for j in range (i+1 , right_2+1):
			if ( j-i < maxlength_2):
				break
			elif string_2[i] == string_2[j]:
				if isPalindrome_2(string_2[i:j+1]):
					length_2 = j - i + 1
					if (length_2 > maxlength_2):
						maxlength_2 = length_2
						maxstring_2 = string_2[i:j+1]

length_of_plaintext = len(plaintext)
encrypted_text = ""
for i in range (1 , length_of_plaintext+1):
	plaintext_i = (ord(plaintext[i-1]) + b) * maxlength_1 + maxlength_2
	plaintext_i = chr(((plaintext_i - 65) % 26) + 65)
	encrypted_text += plaintext_i

print("----- extract key for encypt method -----")
print("The %s-th Fibonacci sequence number is:"%(number),b)
print("Longest palindrome substring within first string is:" , maxstring_1)
print("Length is:" , maxlength_1)
print("Longest palindrome substring within second string is:" , maxstring_2)
print("Length is:" , maxlength_2)
print("----- encryption completed -----")
print("The encrypted text is: " + encrypted_text )








