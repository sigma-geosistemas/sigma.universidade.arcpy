# coding: utf-8
# IDENTACAO

# o python não usa colchetes ou outros delimitadores de bloco
# lembre-se: simplicidade e minimalismo

contador = 0

if contador <= 0:
	# se contador é menor que zero, execute este bloco
	
	print "contador é menor ou igual à zero"
	
	# podemos continuar nosso bloco if
	# a regra é: 4 espaços ou um número de tabs
else:
	# a declaração do else está no mesmo nível do if!
	# mas as instruções do seu bloco estão um tab para frente
	
	print "contador é maior do que zero"
	
	# podemos aninhar expressoes, desde que mantenhamos as tabulações
	
	if contador <= 10:
		
		# dentro do nosso else, temos outra condição e nosso bloco acompanha
		print "é menor do que 10!"
		
	else:
		
		print "é maior do que 10!"
		

print "aqui voltamos para fora do primeiro bloco if"
print "note que estamos no mesmo nível do if inicial"
print "dica: seja consistente! ou use espaços ou use tabulações, mas NÃO misture os dois!"
print "não existe melhor ou pior. só melhor ou pior para você, eu prefiro as tabulações"
	