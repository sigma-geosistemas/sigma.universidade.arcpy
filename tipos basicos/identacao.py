# coding: utf-8
# IDENTACAO

# o python n�o usa colchetes ou outros delimitadores de bloco
# lembre-se: simplicidade e minimalismo

contador = 0

if contador <= 0:
	# se contador � menor que zero, execute este bloco
	
	print "contador � menor ou igual � zero"
	
	# podemos continuar nosso bloco if
	# a regra �: 4 espa�os ou um n�mero de tabs
else:
	# a declara��o do else est� no mesmo n�vel do if!
	# mas as instru��es do seu bloco est�o um tab para frente
	
	print "contador � maior do que zero"
	
	# podemos aninhar expressoes, desde que mantenhamos as tabula��es
	
	if contador <= 10:
		
		# dentro do nosso else, temos outra condi��o e nosso bloco acompanha
		print "� menor do que 10!"
		
	else:
		
		print "� maior do que 10!"
		

print "aqui voltamos para fora do primeiro bloco if"
print "note que estamos no mesmo n�vel do if inicial"
print "dica: seja consistente! ou use espa�os ou use tabula��es, mas N�O misture os dois!"
print "n�o existe melhor ou pior. s� melhor ou pior para voc�, eu prefiro as tabula��es"
	