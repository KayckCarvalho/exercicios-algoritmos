# Estudo de Caso 4 - Controle de Vendas em uma Loja de Eletrônicos
# Contexto do Problema
# Imagine que você trabalha em uma loja de eletrônicos que precisa organizar melhor o registro
# diário de vendas. Até então, os vendedores anotavam em papel ou planilhas, mas o dono pediu
# para criar um programa simples em Python para armazenar, analisar e gerar pequenos
# relatórios sobre as vendas do dia.
# O sistema precisa:
# 1. Guardar os produtos vendidos (nome e preço).
# 2. Mostrar o valor total arrecadado.
# 3. Identificar o produto mais caro e o mais barato do dia.
# 4. Permitir consultar se um produto específico foi vendido.

def registrar_vendas():
    vendas = []
    while True:
        nome = input("Digite o nome do produto (ou 'fim' para encerrar): ")
        if nome.lower() == "fim":
            break
        preco = float(input(f"Digite o preço de {nome}: R$ "))
        vendas.append([nome, preco])
    return vendas

def total_arrecadado(vendas):
    return sum(produto[1] for produto in vendas)

def produtos_extremos(vendas):
    if not vendas:
        return None, None
    mais_caro = max(vendas, key=lambda x: x[1])
    mais_barato = min(vendas, key=lambda x: x[1])
    return mais_caro, mais_barato

def consultar_produto(vendas, nome):
    for produto in vendas:
        if produto[0].lower() == nome.lower():
            return produto
    return None

vendas = registrar_vendas()
total = total_arrecadado(vendas)
mais_caro, mais_barato = produtos_extremos(vendas)

print(f"\nValor total arrecadado: R$ {total:.2f}")
print(f"Produto mais caro: {mais_caro}")
print(f"Produto mais barato: {mais_barato}")

produto_consulta = input("\nDigite o nome do produto para consultar se foi vendido: ")
resultado = consultar_produto(vendas, produto_consulta)
if resultado:
    print(f"O produto {resultado[0]} foi vendido por R$ {resultado[1]:.2f}")
else:
    print(f"O produto {produto_consulta} não foi vendido hoje.")
