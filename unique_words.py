# -*- coding: utf-8 -*-

def unique_words():
	file = open('Machine_learning.txt', encoding='utf-8')
	text = file.read()
	words = []
	raw_text = set(text.split())
	for word in raw_text:
	    if word.isalpha():
	        words.append(word) 

	text = file.close()
	print(words)
	print('У цьому тексті {0} унікальних слів'.format(len(words)))



if __name__ == '__main__':
	unique_words()
