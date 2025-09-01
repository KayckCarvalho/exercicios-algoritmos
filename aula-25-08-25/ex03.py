# Estudo de Caso 3 – Analisando números pares e ímpares
# Enunciado:
# Escreva um programa que:
# 1. Receba 10 números inteiros digitados pelo usuário.
# 2. Separe-os em duas listas: pares e ímpares.
# 3. Exiba quantos números pares e ímpares foram digitados.

def receber_numeros(qtd):
    numeros = []
    for i in range(qtd):
        n = int(input(f"Digite o {i+1}º número: "))
        numeros.append(n)
    return numeros

def separar_pares_impares(numeros):
    pares = [n for n in numeros if n % 2 == 0]
    impares = [n for n in numeros if n % 2 != 0]
    return pares, impares

def mostrar_contagem(pares, impares):
    print(f"Números pares: {pares} (Total: {len(pares)})")
    print(f"Números ímpares: {impares} (Total: {len(impares)})")

numeros = receber_numeros(10)
pares, impares = separar_pares_impares(numeros)
mostrar_contagem(pares, impares)
