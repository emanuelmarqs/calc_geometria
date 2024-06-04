"""Crie um programa que o usuário possa escolher se deseja saber a área de um círculo,
de um triângulo ou de um trapézio."""

import os

#função
def calcular_circulo(raio):
    area = 3.14 * raio**2
    return area  #obs: o return é o fim da função
def calcular_triangulo(base, altura):
    area = base * altura / 2
    return area 
def calcular_trapezio(base1, base0, altura):
    area = (base1 + base0)* altura / 2
    return area 

while True:
# programa principal
    print(f'{"-"*20}MENU{"-"*20}\n')
    print('DIGITE 1 - Para calcular a área de um CÍRCULO: ')
    print('DIGITE 2 - Para calcular a área de um TRIÂNGULO: ')
    print('DIGITE 3 - Para calcular a área de um TRAPÉZIO: ')
    print('Digite 4 para fechar o programa. ')
    print(' ')
    escolha = input('Escolha a forma, que deseja calcular a área: ')

    os.system('cls') #limpa a exibição

    if escolha == '1':
        raio = int(input('Digite o raio do circulo:'))
        print(f'Área do círculo: {calcular_circulo(raio)}')   
    elif escolha == '2':
        base = int(input('Informe a base do triângulo: '))
        altura = int(input('Informe a altura do triângulo: '))
        print(f'Área do triângulo: {calcular_triangulo(base, altura)}') 
    elif escolha == '3':
        base1 = int(input('Informe a base maior do trapézio: '))
        base0 = int(input('Informe a base menor do trapézio: '))
        altura = int(input('Informe a altura do trapézio: '))
        print(f'Área do trapézio: {calcular_trapezio(base1, base0, altura)}') 
    elif escolha == '4':
        break
    else:
        print('Opção inválida!')

