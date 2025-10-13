import random

def busca_pessoa_linear(pessoas, nome):
    """
    Realiza busca linear em uma lista de dicionários para encontrar a pessoa com o nome especificado.
    Retorna o dicionário da pessoa se encontrada, caso contrário None.
    """
    for pessoa in pessoas:
        if pessoa.get("nome") == nome:
            return pessoa
    return None

def jogo_adivinhe_numero():
    """
    Jogo de adivinhação usando lógica de busca binária.
    O computador escolhe um número entre 1 e 100, e o jogador tenta adivinhar.
    O computador dá dicas se o palpite é maior ou menor.
    Conta o número de tentativas.
    """
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    esquerda, direita = 1, 100

    print("Pensei em um número entre 1 e 100. Tente adivinhar!")
    print("Use lógica de busca binária para minimizar tentativas.")

    while True:
        palpite = (esquerda + direita) // 2
        tentativas += 1
        print(f"Tentativa {tentativas}: Palpite {palpite}")

        if palpite == numero_secreto:
            print(f"Acertou! O número era {numero_secreto}. Tentativas: {tentativas}")
            break
        elif palpite < numero_secreto:
            print("Maior")
            esquerda = palpite + 1
        else:
            print("Menor")
            direita = palpite - 1

def buscar_produtos_por_preco(produtos, preco):
    """
    Busca todos os produtos com o preço especificado.
    Retorna uma lista de dicionários dos produtos encontrados.
    """
    encontrados = []
    for produto in produtos:
        if produto.get("preco") == preco:
            encontrados.append(produto)
    return encontrados

def meu_index(lista, valor):
    """
    Implementa a função index() usando busca sequencial.
    Retorna o índice do primeiro valor encontrado, ou levanta ValueError se não encontrado.
    """
    for i, item in enumerate(lista):
        if item == valor:
            return i
    raise ValueError(f"{valor} não está na lista")

if __name__ == "__main__":
    print("Task 11: Busca em Lista de Dicionários")
    pessoas = [
        {"nome": "Ana", "idade": 25},
        {"nome": "João", "idade": 30},
        {"nome": "Maria", "idade": 28}
    ]
    resultado = busca_pessoa_linear(pessoas, "João")
    if resultado:
        print(f"Pessoa encontrada: {resultado}")
    else:
        print("Pessoa não encontrada")

    print("\nTask 12: Jogo: Adivinhe o Número")
    jogo_adivinhe_numero()

    print("\nTask 13: Buscar Produtos por Preço")
    produtos = [
        {"nome": "Produto1", "preco": 10},
        {"nome": "Produto2", "preco": 20},
        {"nome": "Produto3", "preco": 10},
        {"nome": "Produto4", "preco": 30}
    ]
    preco_busca = 10
    encontrados = buscar_produtos_por_preco(produtos, preco_busca)
    print(f"Produtos com preço {preco_busca}: {encontrados}")

    print("\nTask 14: Implementar sua própria função index()")
    lista_exemplo = [1, 2, 3, 4, 5]
    valor_busca = 3
    try:
        indice = meu_index(lista_exemplo, valor_busca)
        print(f"Índice de {valor_busca}: {indice}")
    except ValueError as e:
        print(e)
