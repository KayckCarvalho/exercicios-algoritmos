seu_cpf = input('Digite os 11 digitos que formam o seu cpf:\n >>')
digitos = 11

if seu_cpf.isdigit() and len(seu_cpf) == digitos:
    cpf = int(seu_cpf)
    print(f'O CPF {cpf} é válido.')
else:
    print(f'O CPF {seu_cpf} é inválido!')