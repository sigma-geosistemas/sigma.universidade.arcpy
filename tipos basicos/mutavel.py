lista_a = [1,2,5,99]
lista_b = lista_a

print lista_a

print "a alteração em B, faz A mudar"
lista_b[1] = -100

print "A ",lista_a
print "B ",lista_b

print "isto ocorre pois lista a e lista b apontam para a mesma lista memória"