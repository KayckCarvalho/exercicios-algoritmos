# 3. Crie uma função que verifique se um número é primo.

def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numero = int(input("Digite um número: "))

if eh_primo(numero):
    print(f"{numero} é primo")
else:
    print(f"{numero} não é primo")

