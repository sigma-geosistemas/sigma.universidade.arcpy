# coding: utf-8
import random

def funcao_a():
	print "a"
	
def funcao_b():
	print "b"
	
def funcao_c():
	print "c"
	
def funcao_d():
	print "d"
	
def funcao_e():
	print "e"
	
def funcao_f():
	print "f"
	
switch = { 
			"a" : funcao_a,
			"b" : funcao_b,
			"c" : funcao_c,
			"d" : funcao_d,
			"e" : funcao_e,
			"f" : funcao_f
		 }
		 
def construcao_ifelse(o_escolhido):
	if o_escolhido == "a":
		funcao_a()
	elif o_escolhido == "b":
		funcao_b()
	elif o_escolhido == "c":
		funcao_c()
	elif o_escolhido == "d":
		funcao_d()
	elif o_escolhido == "e":
		funcao_e()
	elif o_escolhido == "f":
		funcao_f()
	else:
		print "não escolheu ninguém que vale a pena"
	
if __name__ == "__main__":
	print "caso deseje sair, aperte ctrl+c!"
	
	while 1:
		possibilidades = "abcdef"
		# ou podemos utilizar a funcao random.choice
		o_escolhido = possibilidades[random.randint(0,len(possibilidades)-1)]

		# executa a funcao referenciada
		switch[o_escolhido]()

