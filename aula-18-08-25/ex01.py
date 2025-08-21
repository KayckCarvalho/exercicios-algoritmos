# 1. Faça um programa que leia dois números e mostre qual é o maior.

def nMaior():
    n1 = float(input("digite o primeiro numero: \n>>"))
    n2 = float(input('Digite o segundo numero: \n>>'))

    if n1 > n2:
        print(f'O maior numero dentre esses dois é {n1}')

    elif n1 < n2:
        print(f'O maior numero dentre esses dois é {n2}')

    else:
        print('São iguais')

nMaior()
        