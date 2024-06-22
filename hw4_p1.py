#H24126094 統計116 李繕安
import random
#建立棋盤格
def grid():
	for i in range(0,20):
		if i == 0:
			print("     a   b   c   d   e   f   g   h   i   ")
		if i % 2 != 0:
			print("   +---+---+---+---+---+---+---+---+---+")
		if i % 2 == 0 and i != 0:
			print(int(i/2)," |   |   |   |   |   |   |   |   |   |")
while True:
	