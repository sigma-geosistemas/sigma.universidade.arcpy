# listas
lista = []
lista.append(99)
lista.append(98)
lista.append(97)
lista.append(96)
lista.append(95)
lista.append("string na lista, pode isso?! pode!")

print lista

# atribui��o fracionada
lista[0:4] = [1,2,3,4,5]
print lista

# ejeta da lista o �ltimo item
print lista.pop()
print lista

# concatena�ao de lista
lista += ["A","B","C"]

# cuidado! este c�digo ir� adicionar um objeto do tipo lista � lista
# aninhando a mesma!
lista.append(["U","LA","LA"])

lista.pop()

# remove o primeiro item da lista
del lista[0]

# podemos atribuir no �ndice
lista[0] = "modificado"

