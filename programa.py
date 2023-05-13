from operacoes import*
lista_numero = []
while True:
 numero = int(input("Informe um número int ou 0 para sair: "))
 if numero == 0:
  break
 lista_numero.append(numero)
soma = operacoes.soma(lista_numero)
media = operacoes.media(lista_numero)
print(f"Soma: {soma}")
print(f"Média: {media}")
