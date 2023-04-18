
# calculo para descobrir se o numero informado pelo usuario é par ou impar

n = float(input("Digite o número para verificar se ele é par ou impar "))
if n%2 == 0:
  print(f"O número {n} é par")
else:
  print(f"O número {n} é impar")

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
