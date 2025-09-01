# Faça um programa que:
# 1. Permita ao usuário adicionar itens a uma lista de compras.
# 2. Caso o usuário digite "sair", o programa encerra.
# 3. Mostre a lista final de compras organizada em ordem alfabética

estoque = []

def armazenamento(estoque):
    while True:
        add = input('Coloque algum item no estoque: \n >>')
        
        pergunta = input('Deseja adicionar mais algo?\n >>')

        if pergunta in ['n', 'não', 'nao']:
            estoque.append(add)
            break
            
        elif pergunta in ['s', 'sim']:
            estoque.append(add)
        
        else:
            print('Comando inválido, tente novamente.')

    estoque.sort()
    for i in estoque:
        print(i, end=', ')
armazenamento(estoque)