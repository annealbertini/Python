#calculando a media das notas (A e B) com pesos

A = float(input())
B = float(input())
MEDIA = (A * 3.5 + B * 7.5) / 11
print(f'MEDIA = {MEDIA:.5f}')


#calculando o consumo medio de litros por km 

X = int(input())
Y = float(input())
consumo_medio = X / Y
print (f'{consumo_medio:.3f}', 'km/l')

#calculando o salario com base em formula definida 

num_funcionario = int(input())
horas_trabalhadas = int(input())
valor_hora = float(input())

salario = horas_trabalhadas * valor_hora

print('NUMBER =', num_funcionario)
print ( f'SALARY = U$ {salario:.2f}')


#calculando o salario com bonus em formula definida 

vendendor = input()
salario_fixo = float(input())
total_vendas = float(input())

comissao = total_vendas * 0.15
salario_total = salario_fixo + comissao

print(f'TOTAL = R$ {salario_total:.2f}')


#calculando a area com formula definida 

A,B,C = input().split(" ")
A = float(A)
B = float(B)
C = float(C)

triretan = A * C /2
areacir = 3.14159 * C ** 2
areatrap = ((A + B)*C / 2)
areaquad = B * B
arearetan = A * B

print(f'TRIANGULO: {triretan:.3f}')
print(f'CIRCULO: {areacir:.3f}')
print(f'TRAPEZIO: {areatrap:.3f}')
print(f'QUADRADO: {areaquad:.3f}')
print(f'RETANGULO: {arearetan:.3f}')

#calculando a distancia entre dois pontos

x1,y1 = input().split()
x2,y2 = input().split()

x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

distancia_1 = (x2 - x1) ** 2 + (y2 - y1) ** 2
distancia_2 = pow(distancia_1, 0.5)
print(f'{distancia_2:.4f}')

#demonstração de algumas operações matematicas basicas no Python

x = float(input('digite o primeiro numero: '))
y = float(input('digite o segundo numero: '))

soma = x+y
subtracao = x-y
multiplicacao = x*y
raiz1 = x**(1/2)
raiz2 = y**(1/2)


print('o valor da soma de {} e {} = {}'.format(x,y,soma))
print('o valor da subtracao de {} e {} = {}'.format(x,y,subtracao))
print('o valor da multiplicacao de {} e {} = {}'.format(x,y,multiplicacao))
print(f'o valor da raiz do primeiro numero {x} é {raiz1:.4f}')
print(f'o valor da raiz do segundo numero {y} é {raiz2:.4f}')

#calculando a area de circuferencia com o raio

import math as ma
raio = float(input('digite o raio da circunferencia: '))
pi = ma.pi
area = pi * raio**2
print('a area da circunferencia é: ', round(area,4))

#executando formula de 2° grau no python

import numpy as np
print ('Vamos calcular a raiz da equacao de 2° grau')
print()
a = float(input('digite o valor de a'))
b = float(input('digite o valor de b'))
c = float(input('digite o valor de c'))

delta = b**2 - 4*a*c

if delta < 0:
  print('como delta é menor que zero na equação nao tem raiz no conjunto dos numeros reais')
else:
    x1 = (b + np.sqrt(delta))/ (2*a)
    x2 = (b - np.sqrt(delta))/ (2*a)
    print(f"As raizes da equacao sao: x1= {x1} e x2 = {x2}")
    
#calculadora de impostos com base no salario e na tabela de impostos do governo

salario = float(input('digite seu salario: '))

if salario <= 1903.99:
   print ('voce esta isento do imposto de renda!')

elif salario >= 1903.99 and salario <= 2826.65:
  salario_atual = salario -(0.075 * salario) + 142
  print ('seu salario apos desconto sera de: ', salario_atual)
  
elif salario >= 2826.66 and salario <= 3751.05:
  salario_atual = salario - (0.15 * salario) + 354.80
  print ('seu salario apos desconto sera de: ', salario_atual)
  
elif salario >= 3751.06 and salario <= 4664.68:
  salario_atual = salario - (0.225 * salario) + 636.13
  print ('seu salario apos desconto sera de: ', salario_atual)
  
elif salario >= 4664.69:
  salario_atual = salario - (0.275 * salario) + 869.36  
print ('seu salario apos desconto sera de: ', salario_atual)
