class listas:
    animais = ['gato', 'cachorro', 'cobra', 'macaco', 'pombo']
    animal_encontrado = False

def buscar_lista(animais):
    nome = input('Digite o nome de um animal:')
    for indice, animal in enumerate(animais, start=1):
        if nome == animal:
            listas.animal_encontrado = True
            return animal, indice
    listas.animal_encontrado = False
    return None, None

if __name__ == "__main__":
    animal_retornado, indice_retornado = buscar_lista(listas.animais)
    if listas.animal_encontrado == True:
        print(f'Animal encontrado: {animal_retornado} na posição {indice_retornado}')
    else:
        print('Nenhum animal encontrado')
