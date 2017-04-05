# -*- coding: utf-8 -*-

lst_input = [1, [2, 3], [[8, 6], [9, 11, 14]], 4, [[6, 7]]]
lst_output = []

def flattern(lst):
	for item in lst:
		#print(item)
		if type(item) == list:
			flattern(item)
		#	print('+')
		else:
			lst_output.append(item)
		#	print('++')
	
	
if __name__ == '__main__':
	flattern(lst_input)
	print('In the end we have:')
	print(lst_output)








