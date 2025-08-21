# 2. Escreva um algoritmo que calcule a tabuada de um número digitado pelo usuário.

n = int(input('Digite um numero:\n >>'))

for x in range(11):
    print(f'{n} X {x} = {x*n}')