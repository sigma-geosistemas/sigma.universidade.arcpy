# coding: utf-8
# arquivos
endereco = "C:\\aerodromo.txt"

arquivo = open(endereco,"r")
aerodromos = []
temp_aerodromo = arquivo.readline()

while temp_aerodromo != "":
	aerodromos.append(temp_aerodromo)
	temp_aerodromo = arquivo.readline()
	
aerodromos.sort()

print "final leitura"
for x in xrange(5):
	print aerodromos[x]
	
