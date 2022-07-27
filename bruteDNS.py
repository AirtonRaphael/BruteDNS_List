import dns.resolver
import sys

resolver = dns.resolver.Resolver()
wordlist = []


try:	# recebe os parametros
	target = sys.argv[1]
	path = sys.argv[2]
except:
	print('Esta faltando argumentos')
	sys.exit()


with open(path, 'r') as file:	#pega o arquivo da wordlist
	wordlist = file.read().splitlines()


try:	# checa o dominio alvo
	brute = resolver.resolve(target, "A")
	for items in brute:
		print(f'{target} --> {items}')
	for Subdomain in wordlist:	#checa os subdominios
		try:

			sub_target = f'{Subdomain}.{target}'
			
			resultados = resolver.resolve(f"{Subdomain}.bancocn.com", "A")

			for resultado in resultados:
				print(f'{Subdomain} --> {resultado}')


		except Exception as error:
			pass
except:
	pass