# Caso3: Supermercado – Controle de Estoque
# Um supermercado mantém uma lista de produtos e seus preços.
# • Cada item será representado como [nome, quantidade, preco_unitario].
# • O sistema deve:
# 1. Calcular o valor total em estoque.
# 2. Encontrar o produto de maior valor total (quantidade × preço).
# 3. Gerar uma lista apenas com os nomes dos produtos com estoque abaixo de 5
# unidades.
# 4. Permitir buscar um produto pelo nome e retornar seus dados.

def valor_total_estoque(produtos):
    total = 0
    for produto in produtos:
        total += produto[1] * produto[2]
    return total

def produto_mais_valioso(produtos):
    max_valor = 0
    produto_valioso = None
    for produto in produtos:
        valor = produto[1] * produto[2]
        if valor > max_valor:
            max_valor = valor
            produto_valioso = produto
    return produto_valioso

def produtos_estoque_baixo(produtos):
    return [produto[0] for produto in produtos if produto[1] < 5]

def buscar_produto(produtos, nome):
    for produto in produtos:
        if produto[0].lower() == nome.lower():
            return produto
    return None

produtos = [
    ["Arroz", 10, 20.0],
    ["Feijão", 3, 15.0],
    ["Macarrão", 8, 5.0],
    ["Óleo", 2, 12.0],
    ["Açúcar", 6, 4.0]
]

total_estoque = valor_total_estoque(produtos)
mais_valioso = produto_mais_valioso(produtos)
estoque_baixo = produtos_estoque_baixo(produtos)
produto_busca = buscar_produto(produtos, "Feijão")

print(f"Valor total em estoque: R$ {total_estoque}")
print(f"Produto de maior valor total: {mais_valioso}")
print(f"Produtos com estoque abaixo de 5 unidades: {estoque_baixo}")
print(f"Produto buscado: {produto_busca}")
