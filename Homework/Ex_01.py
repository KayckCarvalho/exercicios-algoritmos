def contagem_somas(n):
    soma = 0
    operacoes = 0

    for i in range(1,n+1): 
        soma += i 
        operacoes += 1

    return soma, operacoes

n = int(input('Digite um valor inteiro não-negativo:\n>> '))

if n < 0:
    print('Use um n ≥ 0.')
else:
    soma, operacoes = contagem_somas(n)
    formula = n*(n+1)//2

    print(f"""
Soma com loop: {soma}
Operações: {operacoes}
Soma pela fórmula: {formula}
""")

    if soma == formula:
        print('Os dois métodos deram o mesmo resultado.')
    else:
        print('Os resultados não batem — verifique o valor de n.')
