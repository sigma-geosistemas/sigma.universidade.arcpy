# coding: utf-8

def um_oi_da_xurupita(param1,param2="tchau pessoal!"):
	print "param 1",param1
	print "param 2",param2
	
if __name__ == "__main__":
	print "podemos chamar uma funcao de várias formas!"
	
	print "com argumentos posicionais - neste caso todos sao obrigatorios, exceto os com valor default"
	print ""
	
	print "passando todos os argumentos!"
	um_oi_da_xurupita("olá mundão véio sem porteira!","Tchau, foi bom te ver!")
	
	print "com argumentos posicionais, omitindo os opcionais - já que eles tem valor default"
	print ""
	
	print "passando somente os argumentos obrigatórios!"
	um_oi_da_xurupita("neste caso, vamos dar tchau default!")
	
	print "com argumentos nomeados. neste caso, desde que você saiba o nome dos argumentos, a ordem nao importa"
	print ""
	
	print "ou então podemos trocar a ordem de passagem dos argumentos, nomeando-os"
	um_oi_da_xurupita(param2="este é um tchau nomeado.",param1="este é um oi nomeado")