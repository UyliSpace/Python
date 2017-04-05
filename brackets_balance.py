# -*- coding: utf-8 -*-

line = '(((((((((({[2, 3]}))))))))))'

def brackets_balance(text):
	pairs = {'(': ')', '{': '}', '[': ']'}
	counter = 0
	for i in line:
		if i in pairs.keys():
			counter = counter + 1
		#	print(counter)
		elif i in pairs.values():
		    counter = counter - 1
		#    print(counter)
	if counter == 0:
	    print("Всі дужки закриті")
	else:
	    print("Не всі дужки закриті")     


if __name__ == '__main__':
	brackets_balance(line) 

  	

