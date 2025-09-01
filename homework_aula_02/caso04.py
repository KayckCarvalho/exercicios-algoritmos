# Caso4: Análise de Vendas Mensais
# Uma loja online registra o número de vendas de cada dia do mês em uma lista.
# • Exemplo: [10, 15, 20, 5, 0, 8, ...]
# O gerente precisa:
# 1. Calcular o total de vendas no mês.
# 2. Descobrir o dia com mais vendas e o dia com menos vendas.
# 3. Calcular a média de vendas por dia.
# 4. Listar os dias que tiveram vendas acima da média.

def total_vendas(vendas):
    return sum(vendas)

def dias_extremos(vendas):
    dia_mais_vendas = vendas.index(max(vendas)) + 1  
    dia_menos_vendas = vendas.index(min(vendas)) + 1
    return dia_mais_vendas, dia_menos_vendas

def media_vendas(vendas):
    return sum(vendas) / len(vendas)

def dias_acima_media(vendas):
    media = media_vendas(vendas)
    return [i+1 for i, v in enumerate(vendas) if v > media]  

vendas_mes = [10, 15, 20, 5, 0, 8, 12, 18, 7, 14, 6, 9, 11, 16, 13, 4, 2, 19, 21, 17, 3, 10, 8, 12, 15, 7, 6, 9, 14, 5]

total = total_vendas(vendas_mes)
mais_vendas, menos_vendas = dias_extremos(vendas_mes)
media = media_vendas(vendas_mes)
acima_media = dias_acima_media(vendas_mes)

print(f"Total de vendas no mês: {total}")
print(f"Dia com mais vendas: {mais_vendas}")
print(f"Dia com menos vendas: {menos_vendas}")
print(f"Média de vendas por dia: {media:.2f}")
print(f"Dias com vendas acima da média: {acima_media}")
