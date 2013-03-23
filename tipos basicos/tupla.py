# tupla vazia
tupla = ()

# declaração de tuplas, com e sem parenteses
tupla_um = (1,)
tupla_do = 1,

# confirma o tipo
type(tupla_um)
type(tupla_do)

# iteracao
tupla = ("um","dois","tres",)
for x in tupla:
	print x
	
# pertencimento
if "um" in tupla:
	print "está aqui"
	
# não podemos ordenar uma tupla
# ERRO
tupla.sort()

# nem alterar localmente os itens
# ERRO
tupla[0] = "um modificado"

# mas podemos fracionar
tu2 = tupla[1:2]

# e indexar
um = tupla[0]
