# coding: utf-8
import copy
lista_a = [1,2,5,99]
lista_b = lista_a

print lista_a

print "a alteração em B, faz A mudar"
lista_b[1] = -100

print "A ",lista_a
print "B ",lista_b

print "isto ocorre pois lista a e lista b apontam para a mesma lista memoria"

print "ao usar copy.copy isto não ocorre. temos uma cópia fiel, mas em outro endereco de memoria"
lista_b = copy.copy(lista_a)

lista_b[1] = -200

print "A ", lista_a
print "B ", lista_b