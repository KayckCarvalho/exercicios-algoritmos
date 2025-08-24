# 4. Desenvolva um programa que leia uma lista de números e mostre a média deles

numeros = [4, 5, 6]
soma = 0

for n in numeros:
    print(f"{n} ", end="")
    soma += n

media = soma /len(numeros)

print(f"\n média dos numeros: \n {media}")


