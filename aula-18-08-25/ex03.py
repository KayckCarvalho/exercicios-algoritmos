# 3. Crie uma função que verifique se um número é primo.

def nprimo():
    x = 2
    n = int(input('Digite um numero:\n >>'))
    if n / 1 == n and n / n == 1 and n % x == 0 and n % 3 == 0 and n % 5 == 0 and n % 7 == 0 and n % 9 == 0:
        print(f'o numero {n} não é primo')
    else:
        print(f'o numero {n} é um numero primo')
                
nprimo()