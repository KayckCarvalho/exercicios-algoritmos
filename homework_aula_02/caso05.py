# Caso5: Controle de Participação em um Evento
# Os organizadores de um evento registraram os nomes dos participantes de cada atividade em
# listas separadas.
# • Exemplo:
# o Palestra: ["Ana", "Carlos", "Marina"]
# o Workshop: ["Carlos", "João", "Ana"]
# o Mesa-redonda: ["Marina", "João", "Paula"]
# Eles precisam:
# 1. Saber quem participou de todas as atividades.
# 2. Saber quem participou de apenas uma atividade.
# 3. Gerar uma lista com todos os nomes únicos dos participantes.
# 4. Contar quantos participantes distintos houve no evento.

def participantes_todas_atividades(atividades):
    conjuntos = [set(lista) for lista in atividades.values()]
    participantes_todos = set.intersection(*conjuntos)
    return participantes_todos

def participantes_uma_atividade(atividades):
    todos = []
    for lista in atividades.values():
        todos.extend(lista)
    contagem = {}
    for participante in todos:
        contagem[participante] = contagem.get(participante, 0) + 1
    apenas_uma = [p for p, c in contagem.items() if c == 1]
    return apenas_uma

def todos_participantes(atividades):
    nomes = set()
    for lista in atividades.values():
        nomes.update(lista)
    return nomes

def total_participantes(atividades):
    return len(todos_participantes(atividades))

atividades = {
    "Palestra": ["Ana", "Carlos", "Marina"],
    "Workshop": ["Carlos", "João", "Ana"],
    "Mesa-redonda": ["Marina", "João", "Paula"]
}

todos = participantes_todas_atividades(atividades)
uma_atividade = participantes_uma_atividade(atividades)
nomes_unicos = todos_participantes(atividades)
total = total_participantes(atividades)

print("Participantes de todas as atividades:", todos)
print("Participantes de apenas uma atividade:", uma_atividade)
print("Todos os participantes únicos:", nomes_unicos)
print("Total de participantes distintos:", total)
