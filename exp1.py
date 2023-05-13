from pacote import *
print('Bem vindo a calculadora')
num1=int(input('Digite o primeiro numero: '))
num2=int(input('Digite o segundo numero: '))
op = int(input('Digite 1 para somar e 2 para subtrair'))
if op == 1:
 print(f'O valor de soma {num1} e {num2} é {soma.calcular(num1,num2)}')
elif op ==2:
 print(f'O valor da subtração {num1} e {num2} é {sub.calcular(num1,num2)}')
else:
 print('Comando invalido!!')