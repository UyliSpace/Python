# -*- coding: utf-8 -*-

def general(text):
	def child(word):
		return ("{0} it\'s {1}".format(name, word))
	return child


fun = general('foo')
print(fun('bar'))
