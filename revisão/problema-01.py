# Problema 1 – Restaurante Inteligente
# Um restaurante armazena os pedidos do dia em uma lista de dicionários, onde cada pedido tem:
# cliente, itens (lista de dicionários com prato e preco).
# Tarefas:
# 1. Crie uma função que receba o nome de um cliente e retorne o valor total gasto (somando
# todos os itens pedidos).
# 2. Crie uma função que descubra qual prato foi o mais vendido no dia.
# 3. Mostre um ranking com os 3 clientes que mais gastaram, em ordem decrescente.

pedidos = []

def add_cliente():
    while True:
        nome_cliente = input('Digite o nome do cliente:\n >> ')
        numero_pratos = int(input('Digite a quantidade de pedidos: \n >> '))
        
        itens = []
        for i in range(numero_pratos):
            nome_prato = input('Digite o nome do prato: \n >> ')
            preco = float(input('Digite o preço do pedido: \n >> '))
            itens.append({"prato": nome_prato, "preço": preco})
        
        pedidos.append({"Cliente": nome_cliente, "itens": itens})
        
        pergunta = input('Deseja adicionar mais algum cliente? (s/n)\n >> ')
        if pergunta.lower() not in ['s', 'sim']:
            break

def total_gasto_cliente(nome):
    total = 0
    for pedido in pedidos:
        if pedido["Cliente"] == nome:
            for item in pedido["itens"]:
                total += item["preço"]
    return total

def mais_vendido():
    contagem = {}
    for pedido in pedidos:
        for item in pedido["itens"]:
            prato = item["prato"]
            contagem[prato] = contagem.get(prato, 0) + 1
    mais_vendido = max(contagem, key=contagem.get)
    return mais_vendido

def ranking_clientes():
    gastos = {}
    for pedido in pedidos:
        cliente = pedido["Cliente"]
        total = sum(item["preço"] for item in pedido["itens"])
        gastos[cliente] = gastos.get(cliente, 0) + total
    ranking = sorted(gastos.items(), key=lambda x : x[1], reverse=True)
    return ranking[:3]

print('=== RESTAURANTE DO JOSÉ ===')
add_cliente()

print('\n--- Pedidos ---')
for p in pedidos:
    print(p)

print('\n--- Prato mais vendido ---')
print(mais_vendido())

print('\n--- Ranking dos 3 clientes que mais gastaram ---')
for i, (cliente, valor) in enumerate(ranking_clientes(), 1):
    print(f"{i}. {cliente} - R$ {valor:.2f}")


