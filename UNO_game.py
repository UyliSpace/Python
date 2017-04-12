# -*- coding: utf-8 -*-

import random 


COMPUTER_NAME = 'Комп\'ютер'


cards_suit = ['♠', '♣', '♦', '♥']

deck = [('6','♠'), ('6', '♣'), ('6', '♦'), ('6', '♥'),
	    ('7', '♠'), ('7', '♣'), ('7', '♦'), ('7', '♥'),
	    ('8', '♠'), ('8', '♣'), ('8', '♦'), ('8', '♥'),
	    ('9', '♠'), ('9', '♣'), ('9', '♦'), ('9', '♥'),
	    ('10', '♠'), ('10', '♣'), ('10', '♦'), ('10', '♥'),
	    ('J', '♠'), ('J', '♣'), ('J', '♦'), ('J', '♥'),
	    ('Q', '♠'), ('Q', '♣'), ('Q', '♦'), ('Q', '♥'),
	    ('K', '♠'), ('K', '♣'), ('K', '♦'), ('K', '♥'),
	    ('A', '♠'), ('A', '♣'), ('A', '♦'), ('A', '♥')
	    ]
random.shuffle(deck)

def generate_cards(cards):
	while len(cards) < 6:
		generate_cards = deck.pop()
		cards.append(generate_cards)
	return(cards)

def interface(comp_cards, current_card, user_cards, user_name):
	print("")
	print("================================================")
	print("\t\t", COMPUTER_NAME)
	print("")
	print("\t\t {} карт".format(len(comp_cards)))
	print("")
	print("")
	print("\t\t", current_card)   # carta iakou poxodulu
	print("")
	print("")
	for i in user_cards:
	    print("\t\t {}".format(i))
	print("")
	print("\t\t", user_name)
	print("================================================")
	print("")

def user_go(user_cards, current_card):
	user_available_cards = []
	user_cards_choice = {}
	number_card = 1
	for item in user_cards:
		for i in item:
			if i == current_card[0]:
				user_available_cards.append((item[0], item[1]))
				user_cards_choice[number_card] = (item[0], item[1])
				number_card = number_card + 1
			elif i == current_card[1]:
				user_available_cards.append((item[0], item[1]))	
				user_cards_choice[number_card] = (item[0], item[1])
				number_card = number_card + 1
			else:
				pass
	if user_cards_choice:
		print("")
		print("Чим походите?")
		print(user_cards_choice)
		user_choice = input()
		mix = user_cards_choice[int(user_choice)]
		print(mix)
		current_card = user_cards.pop(mix)
		print(current_card)
		print(user_cards)
		
	else:
		exit()
	return current_card, user_cards
	

def computer_go(comp_cards, current_card):
	comp_available_cards = []
	for item in comp_cards:
		for i in item:
			if i == current_card[0]:
				comp_available_cards.append((item[0], item[1]))
			elif i == current_card[1]:
				comp_available_cards.append((item[0], item[1]))
			else:
				pass
	if comp_available_cards:
	    comp_choice = random.choice(comp_available_cards)
	    #print(comp_choice)
	    current_card = comp_choice
	    #print(current_card)
	    #comp_cards.pop(current_card)
	else:
		exit()
	return current_card, comp_cards




if __name__ == '__main__':
	print("\tВІТАЄМО В ГРІ \'UNO\'")
	print("Ваше ім\'я?\n")
	user_name = input()
	names = []
	names.append(COMPUTER_NAME)
	names.append(user_name)
	user_cards = []
	comp_cards = []
	user_cards = generate_cards(user_cards)
	comp_cards = generate_cards(comp_cards)
	current_card = deck.pop()

	#while deck:
	first_step = random.choice(names)
	print('Першим ходить - {}'.format(first_step))
	if first_step == COMPUTER_NAME:
		interface(comp_cards, current_card, user_cards, user_name)
		computer_go(comp_cards, current_card)
		user_go(user_cards, current_card)
		
		interface(comp_cards, current_card, user_cards, user_name)

	else:
		interface(comp_cards, current_card, user_cards, user_name)
		user_go(user_cards, current_card)
		
		computer_go(comp_cards, current_card)
		interface(comp_cards, current_card, user_cards, user_name)
