import math

def analise_vendas_mensais():
    vendas = {
        dia: valor for dia, valor in enumerate(
            [10, 15, 20, 5, 0, 8, 12, 17, 21, 7, 13, 25, 6, 18, 9,
             14, 22, 11, 19, 3, 16, 8, 12, 15, 20, 4, 10, 7, 13, 9],
            start=1
        )
    }

    total = sum(vendas.values())

    dia_max = max(vendas, key=vendas.get)
    dia_min = min(vendas, key=vendas.get)

    media = total / len(vendas)

    dias_acima_media = [dia for dia, v in vendas.items() if v > media]

    print("=== Análise de Vendas Mensais ===")
    print(f"Total de vendas no mês: {total}")
    print(f"Dia com mais vendas: {dia_max} ({vendas[dia_max]} vendas)")
    print(f"Dia com menos vendas: {dia_min} ({vendas[dia_min]} vendas)")
    print(f"Média de vendas/dia: {media:.2f}")
    print(f"Dias com vendas acima da média: {dias_acima_media}")

analise_vendas_mensais()
