import time
def busca_nome_linear():
    nomes = []
    print("Digite os nomes (digite 'fim' para parar):")
    while True:
        nome = input("Nome: ")
        if nome.lower() == 'fim':
            break
        nomes.append(nome)
    nome_procurado = input("Digite o nome a procurar: ")
    for i, nome in enumerate(nomes):
        if nome == nome_procurado:
            print(f"Nome encontrado na posição {i}")
            return
    print("Nome não encontrado")

def busca_binaria_recursiva(arr, alvo, esquerda=0, direita=None):
    if direita is None:
        direita = len(arr) - 1
    if esquerda > direita:
        return -1
    meio = (esquerda + direita) // 2
    if arr[meio] == alvo:
        return meio
    elif arr[meio] < alvo:
        return busca_binaria_recursiva(arr, alvo, meio + 1, direita)
    else:
        return busca_binaria_recursiva(arr, alvo, esquerda, meio - 1)

def comparar_tempos():

    lista = list(range(1000000))
    alvo = 999999 

    inicio = time.time()
    for i in range(len(lista)):
        if lista[i] == alvo:
            break
    tempo_linear = time.time() - inicio

    inicio = time.time()
    busca_binaria_recursiva(lista, alvo)
    tempo_binaria = time.time() - inicio

    print(f"Tempo Busca Linear: {tempo_linear:.6f} segundos")
    print(f"Tempo Busca Binária: {tempo_binaria:.6f} segundos")

def primeira_ocorrencia(arr, alvo):
    esquerda, direita = 0, len(arr) - 1
    resultado = -1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if arr[meio] == alvo:
            resultado = meio
            direita = meio - 1  
        elif arr[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return resultado

def localizar_intervalo(arr, alvo):
    inicio = primeira_ocorrencia(arr, alvo)
    if inicio == -1:
        return (-1, -1)
    esquerda, direita = inicio, len(arr) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if arr[meio] == alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    fim = direita
    return (inicio, fim)

if __name__ == "__main__":
    busca_nome_linear()

    lista_ordenada = [1, 3, 5, 7, 9, 11]
    alvo = 7
    indice = busca_binaria_recursiva(lista_ordenada, alvo)
    print(f"\nÍndice de {alvo}: {indice}")

    comparar_tempos()

    lista_com_repetidos = [1, 2, 2, 2, 3, 4, 5]
    alvo = 2
    indice_primeiro = primeira_ocorrencia(lista_com_repetidos, alvo)
    print(f"\nPrimeira ocorrência de {alvo}: {indice_primeiro}")

    intervalo = localizar_intervalo(lista_com_repetidos, alvo)
    print(f"\nIntervalo de {alvo}: {intervalo}")
