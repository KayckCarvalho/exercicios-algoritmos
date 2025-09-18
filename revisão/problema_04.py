# Você recebeu uma lista de filmes (cada filme é um dicionário) com os campos:
# • titulo → nome do filme
# • diretor → nome do diretor
# • bilheteria → valor em milhões de dólares
# • avaliacoes → lista de notas de 1 a 10
# Tarefas:
# 1. Top 3 maiores bilheterias
# o Crie uma função top_bilheteria(filmes) que retorne os 3 filmes com maior
# bilheteria.
# 2. Top 3 melhores avaliados
# o Crie uma função top_avaliacao(filmes) que calcule a média das avaliações de
# cada filme e retorne os 3 melhores.
# 3. Bilheteria por diretor
# o Crie uma função bilheteria_por_diretor(filmes) que retorne um dicionário onde a
# chave é o diretor e o valor é o total de bilheteria de todos os seus filmes.
# 4. Campeão absoluto
# o Crie uma função campeao(filmes) que mostre qual filme é a melhor combinação
# de bilheteria alta e avaliação média alta.

filmes = [
    {
        "titulo": "Inception",
        "diretor": "Christopher Nolan",
        "bilheteria": 829.9,
        "avaliacoes": [9, 8, 10, 9, 9]
    },
    {
        "titulo": "The Dark Knight",
        "diretor": "Christopher Nolan",
        "bilheteria": 1004.6,
        "avaliacoes": [10, 9, 10, 10, 9]
    },
    {
        "titulo": "Interstellar",
        "diretor": "Christopher Nolan",
        "bilheteria": 677.5,
        "avaliacoes": [8, 9, 9, 8, 9]
    },
    {
        "titulo": "Pulp Fiction",
        "diretor": "Quentin Tarantino",
        "bilheteria": 213.9,
        "avaliacoes": [9, 10, 10, 9, 8]
    },

]

def top_bilheteria(filmes):
    top_3 = sorted(filmes, key=lambda x: x["bilheteria"], reverse=True)[:3]
    print("Top 3 maiores bilheterias:")
    for filme in top_3:
        print(f'{filme["titulo"]} - ${filme["bilheteria"]}M')

def top_avaliacao(filmes):
    for filme in filmes:
        if filme["avaliacoes"]:
            filme["media_avaliacao"] = sum(filme["avaliacoes"]) / len(filme["avaliacoes"])
        else:
            filme["media_avaliacao"] = 0
    top_3 = sorted(filmes, key=lambda x: x["media_avaliacao"], reverse=True)[:3]
    print("\nTop 3 melhores avaliados:")
    for filme in top_3:
        print(f'{filme["titulo"]} - Média de Avaliação: {filme["media_avaliacao"]:.2f}')

def bilheteria(filmes):
    bilheteria_diretor = {}
    for filme in filmes:
        diretor = filme["diretor"]
        bilheteria_diretor[diretor] = bilheteria_diretor.get(diretor, 0) + filme["bilheteria"]
    print("\nBilheteria por diretor:")
    for diretor, total in bilheteria_diretor.items():
        print(f'{diretor} - Total de Bilheteria: ${total}M')

def campeao(filmes):
    for filme in filmes:
        if filme["avaliacoes"]:
            filme["media_avaliacao"] = sum(filme["avaliacoes"]) / len(filme["avaliacoes"])
        else:
            filme["media_avaliacao"] = 0
        filme["score"] = filme["bilheteria"] * filme["media_avaliacao"]
    campeao = max(filmes, key=lambda x: x["score"])
    print(f'\nCampeão absoluto: {campeao["titulo"]} - Bilheteria: ${campeao["bilheteria"]}M, Média de Avaliação: {campeao["media_avaliacao"]:.2f}, Score: {campeao["score"]:.2f}')

top_bilheteria(filmes)
top_avaliacao(filmes)
bilheteria(filmes)
campeao(filmes)
