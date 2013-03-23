# coding: utf-8
import random

if __name__ == "__main__":
	
	print "agora vamos aos exemplos"
	
	print "vamos aos exemplos"
	print ""
	
	print "vamos gerar um numero aleatorio entre 0 e 99 com randint"
	random.randint(0,99)
	
	print ""
	
	print "agora vamos gerar um numero com randrange. randrange é legal pois nois deixa escolher um step"
	random.randrange(0,99)
	
	print ""
	print "vamos escolher um item aleatorio de uma lista. humn, poderoso"
	print "criando lista de inteiros 1 à 10"
	lista = range(1,11)
	print lista
	
	random.choice(lista)
	
	print ""
	print "alem disso, podemos embaralhar sequencias. lembra da nossa listinha organizada de 1 a 10?"
	random.shuffle(lista)
	print lista
	
	print ""
	print "esta funcao aqui e poderosa! podemos criar uma amostragem de uma sequencia totalmente aleatoria, com uma linha!"
	print "nossa lista sera a string 'aprendendo python e gis'"
	variavel = "aprendendo python e gis"
	
	print "nossa amostra de tres elementos e"
	
	print random.sample(variavel,3)
	print "nossa amostra de dez elementos e"
	print random.sample(variavel,10)

	raw_input("digite algo para sair")

	