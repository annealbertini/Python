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




