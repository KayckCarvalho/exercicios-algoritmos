import random

def criar_mapa(mapa):
    for i in range(5):
        linha = []
        for j in range(5):
            linha.append('~')
        mapa.append(linha)

def mostrar_mapa(mapa):
    for i in mapa:
        for k, j in enumerate(i):
            print(f'{j}', end=' ')
            if k == len(mapa)-1:
                print('')

def atualizar_mapa(mapa, linha, coluna):
    linha_correta, coluna_correta = verificar_escolha(linha, coluna)
    mapa[linha][coluna] = "X"
    if linha_correta == 0 and coluna_correta == 0:
        mapa[linha][coluna] = "T"

def verificar_escolha(linha, coluna):
    resposta_linha = 0
    resposta_coluna = 0

    if linha > LINHA_CORRETA: 
        resposta_linha = 1
    elif linha < LINHA_CORRETA:
        resposta_linha = -1
    
    if coluna > COLUNA_CORRETA:
        resposta_coluna = -1
    elif coluna < COLUNA_CORRETA:
        resposta_coluna = 1

    return resposta_linha, resposta_coluna

def inputs_validos(linha, coluna, mapa):
    if not linha.isdigit() or not coluna.isdigit():
        return False
    linha = int(linha)
    coluna = int(coluna)
    if linha not in range(len(mapa)) or coluna not in range(len(mapa)):
        return False
    return True

def dar_dica(linha_correta, coluna_correta):
    dica_linha = 'nesta linha'
    dica_coluna = 'nesta coluna'

    if linha_correta == 1:
        dica_linha = 'Mais para cima'
    elif linha_correta == -1:
        dica_linha = 'mais para baixo'
    
    if coluna_correta == 1:
        dica_coluna = 'mais para a direita'
    elif coluna_correta == -1:
        dica_coluna = 'mais para a esquerda'

    print(f'DICA: O tesouro está {dica_linha} e {dica_coluna}.\n')

LINHA_CORRETA = random.randint(0, 4)
COLUNA_CORRETA = random.randint(0, 4)
tentiva = 1
mapa = []
criar_mapa(mapa)

print("=== Caça ao tesouro ===")
while tentiva <= 7:
    print("\n=== Tabuleiro ===")
    mostrar_mapa(mapa)
    print(f'\ntentativa {tentiva} de 7')
    linha = input('Escolha uma linha (0-4): ')
    coluna = input('escolha uma coluna (0-4): ')

    if not inputs_validos(linha, coluna, mapa):
        print("Linha e/ou coluna inválidos. Tente novamente\n")
        continue
    linha = int(linha)
    coluna = int(coluna)
    l_correta, c_correta = verificar_escolha(linha, coluna)
    atualizar_mapa(mapa, linha, coluna)

    if l_correta == 0 and c_correta == 0:
        print("VOCÊ ENCONTROU O TESOURO!\n")
        mostrar_mapa(mapa)
        break

    if tentiva == 7:
        print("VOCÊ NÃO ENCONTROU O TESOURO!")
        print(f"Localização: Linha {LINHA_CORRETA} | Coluna {COLUNA_CORRETA}\n")
        atualizar_mapa(mapa ,LINHA_CORRETA, COLUNA_CORRETA)
        mostrar_mapa(mapa)
        tentiva += 1
        continue

    dar_dica(l_correta, c_correta)
    tentiva += 1
print("FIM DE JOGO")