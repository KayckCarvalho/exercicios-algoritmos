# Uma loja virtual armazena músicas em uma lista de dicionários, cada música com:
# titulo, artista, downloads, avaliacoes (lista de notas de 1 a 5).
# Tarefas:
# 1. Crie uma função que calcule a nota média de avaliação de cada música.
# 2. Crie uma função que mostre qual artista tem o maior número total de downloads
# somando todas as suas músicas.
# 3. Monte um ranking das músicas mais bem avaliadas (ordem decrescente da média das
# notas).

musicas = [
    {
        "titulo": "Shape of You",
        "artista": "Ed Sheeran",
        "downloads": 1500000,
        "avaliacoes": [5, 4, 5, 4, 5]
    },
    {
        "titulo": "Blinding Lights",
        "artista": "The Weeknd",
        "downloads": 2000000,
        "avaliacoes": [5, 5, 4, 5, 5]
    },
    {
        "titulo": "Levitating",
        "artista": "Dua Lipa",
        "downloads": 1200000,
        "avaliacoes": [4, 4, 5, 4, 4]
    },
    {
        "titulo": "Peaches",
        "artista": "Justin Bieber",
        "downloads": 1800000,
        "avaliacoes": [5, 5, 5, 4, 5]
    },
    {
        "titulo": "Save Your Tears",
        "artista": "The Weeknd",
        "downloads": 1600000,
        "avaliacoes": [4, 5, 4, 5, 4]
    }
]

def media():
    for musica in musicas:
        if musica["avaliacoes"]:
            media_avaliacao = sum(musica["avaliacoes"]) / len(musica["avaliacoes"])
            print(f'Média de avaliação de "{musica["titulo"]}": {media_avaliacao:.2f}')
        else:
            print(f'"{musica["titulo"]}" não possui avaliações.')

def mais_baixado():
    downloads_por_artista = {}
    for musica in musicas:
        artista = musica["artista"]
        downloads_por_artista[artista] = downloads_por_artista.get(artista, 0) + musica["downloads"]
    
    artista_mais_baixado = max(downloads_por_artista, key=downloads_por_artista.get)
    total_downloads = downloads_por_artista[artista_mais_baixado]
    print(f'Artista com mais downloads: {artista_mais_baixado} ({total_downloads} downloads)')

def ranking():
    musicas_com_media = []
    for musica in musicas:
        if musica["avaliacoes"]:
            media_avaliacao = sum(musica["avaliacoes"]) / len(musica["avaliacoes"])
            musicas_com_media.append((musica["titulo"], media_avaliacao))
    
    musicas_com_media.sort(key=lambda x: x[1], reverse=True)
    
    print('Ranking das músicas mais bem avaliadas:')
    for i, (titulo, media_avaliacao) in enumerate(musicas_com_media, start=1):
        print(f'{i}. {titulo} - Média de avaliação: {media_avaliacao:.2f}')
    
media()
mais_baixado()
ranking()