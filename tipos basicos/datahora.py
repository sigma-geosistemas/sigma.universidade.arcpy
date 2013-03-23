# coding: utf-8
import datetime

print "vamos pegar o horario de inicio do script"
inicio = datetime.datetime.now()

print "podemos pegar a data de hoje! (cuidado, today é uma funcao)"
datetime.date.today()

print "podemos pegar a data e hora!"
datetime.datetime.now()

print "vamos calcular um delta de tempo"
fim = datetime.datetime.now()

fim - inicio
