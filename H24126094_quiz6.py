#H24126094 統計116 李繕安

#引用隨機函數
import random

#建立英文字母表並分段
_1alphabet = ["a","b","c","d"]
_2alphabet = ["e","f","g","h"]
_3alphabet = ["i","j","k","l"]
_4alphabet = ["m","n","o","p"]
_5alphabet = ["q","r","s","t"]
_6alphabet = ["u","v","w","x"]
_7alphabet = ["y","z"]
all_alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#利用隨機函數建立答案
random.shuffle(all_alphabet)
answer = all_alphabet.pop(0)

#計算猜的次數
def calculate():
	if enter in all_alphabet:
		if enter in _1alphabet:
			cal_1 += 1
		elif enter in _2alphabet:
			cal_2 += 1
		elif enter in _3alphabet:
			cal_3 += 1
		elif enter in _4alphabet:
			cal_4 += 1
		elif enter in _5alphabet:
			cal_5 += 1
		elif enter in _6alphabet:
			cal_6 += 1
		elif enter in _7alphabet:
			cal_7 += 1
	else:
		print("Please enter a lowercase alphabet.")
	return cal

enter = str(input("Guess the lowercase alphabet: "))

