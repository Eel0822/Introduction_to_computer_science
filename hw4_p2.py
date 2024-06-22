#H24126094 統計116 李繕安
import random
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["C", "D", "H", "S"]

def ShuffleDeck():
	deck = []
	for i in suits:
		for j in ranks:
			deck.append(i+j)
	random.suffle(deck)
	return deck

def DrawCards(deck,num):
	cards = []
	for i in range(num):
		card = deck.pop(0)
		cards.appens(card)
	return cards

def calculate_value(hand):
	total_value = 0
	for card in hand:
		card_value = card[1:]
		if card_value == "A":
			if total_value <= 10:
				total_value += 11
			else:
				total_value += 1
		elif card_value in ["J", "Q", "K"]
			total_value += 10
		else:
			total_value += int(card_value)
	return total_value

deck = ShuffleDeck()
player = DrawCards(deck,2)
dealer = DrawCards(deck,2)
total_value_p = calculate_value(player)
total_value_d = calculate_value(dealer)

print("Your current value is",tol_value_p)
print("With the hand",player)
while tol_value_p < 21:
	hs_ornot = int(input("\nHit or Stay? (Hit = 1, Stay = 0): "))
	print()
	if hs_ornot == 1:
		card = deck.pop(0)
		print("You draw",card)
		print()
		player.append(card)
		tol_value_p = cal_card_value(player)
		if tol_value_p <= 21:
			print("Your current value is",tol_value_p)
			print("With the hand",player)
	else:
		print("")
		break

if tol_value_p== 21:
	print("\nBlack jack")
elif tol_value_p >21:
	print("Bust!(>21)")

print("---------------------------------------------\n")

print("Dealer's current value is",tol_value_d)
print("With the hand",dealer)
while tol_value_d < 21 :
	while tol_value_d <= 17:
		card = deck.pop(0)
		print("\nDealer draw",card)
		dealer.append(card)
		tol_value_d = cal_card_value(dealer)	#返回更新後的總點數
		print("\nDealer's current value is",tol_value_d)
		print("With the hand",dealer)
	if tol_value_d > 17:
		break
if tol_value_d== 21:
	print("\nBlack jack")
elif tol_value_d >21:
	print("\nBust!(>21)")

print()
if tol_value_p <= 21 and tol_value_d <= 21:
	if tol_value_p > tol_value_d:
		print("~~~You beat the dealer!~~~")
	elif tol_value_p < tol_value_d:
		print("~~~Dealer wins~~~")
	elif tol_value_p == tol_value_d:
		print("~~~You tied the dealer, nobody wins~~~")

elif tol_value_p > 21 and tol_value_d > 21:
	print("~~~You tied the dealer, nobody wins~~~")
elif tol_value_p <= 21 and tol_value_d > 21:
	print("~~~You beat the dealer!~~~")
elif tol_value_p > 21 and tol_value_d <= 21:
	print("~~~Dealer wins~~~")