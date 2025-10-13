def busca_linear(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return f"Elemento {alvo} encontrado no índice {i}."
    return f"Elemento {alvo} não encontrado."


def contar_ocorrencias(lista, alvo):
    contador = 0
    for elemento in lista:
        if elemento == alvo:
            contador += 1
    return f"O número {alvo} aparece {contador} vez(es)."


def maior_numero(lista):
    if not lista:
        return "Lista vazia."
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    return f"O maior número é {maior}."


def menor_numero(lista):
    if not lista:
        return "Lista vazia."
    menor = lista[0]
    for numero in lista:
        if numero < menor:
            menor = numero
    return f"O menor número é {menor}."


def busca_binaria(lista_ordenada, alvo):
    inicio = 0
    fim = len(lista_ordenada) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista_ordenada[meio] == alvo:
            return f"Elemento {alvo} encontrado no índice {meio}."
        elif lista_ordenada[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return f"Elemento {alvo} não encontrado."


def exibir_menu():
    print("\n--- MENU ---")
    print("1. Busca Linear Simples")
    print("2. Contar Ocorrências (Busca Linear)")
    print("3. Maior Número (Busca Linear)")
    print("4. Menor Número (Busca Linear)")
    print("5. Verificar Elemento (Busca Binária)")
    print("0. Sair")


def main():
    lista = input("Digite os números da lista separados por espaço: ")
    lista = [int(x) for x in lista.split()]

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            alvo = int(input("Digite o número a buscar: "))
            print(busca_linear(lista, alvo))

        elif opcao == "2":
            alvo = int(input("Digite o número para contar ocorrências: "))
            print(contar_ocorrencias(lista, alvo))

        elif opcao == "3":
            print(maior_numero(lista))

        elif opcao == "4":
            print(menor_numero(lista))

        elif opcao == "5":
            lista_ordenada = sorted(lista)
            print(f"Lista ordenada para busca binária: {lista_ordenada}")
            alvo = int(input("Digite o número a buscar: "))
            print(busca_binaria(lista_ordenada, alvo))

        elif opcao == "0":
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
