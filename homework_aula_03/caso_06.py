def sistema_biblioteca():
    biblioteca = {
        "Dom Casmurro": {"usuario": "Ana", "dias": 5},
        "1984": {"usuario": "Carlos", "dias": 12},
        "O Hobbit": {"usuario": "Marina", "dias": 3},
        "A Revolução dos Bichos": {"usuario": "João", "dias": 15},
        "It": {"usuario": "Paula", "dias": 9}
    }

    livros_7dias = [titulo for titulo, dados in biblioteca.items() if dados["dias"] > 7]

    livro_mais_tempo = max(biblioteca, key=lambda t: biblioteca[t]["dias"])

    usuarios = list({dados["usuario"] for dados in biblioteca.values()})

    media_dias = sum(dados["dias"] for dados in biblioteca.values()) / len(biblioteca)

    print("\n=== Sistema de Biblioteca ===")
    print("Livros emprestados há mais de 7 dias:", livros_7dias)
    print(f"Livro emprestado há mais tempo: {livro_mais_tempo} ({biblioteca[livro_mais_tempo]['dias']} dias)")
    print("Usuários com livros emprestados:", usuarios)
    print(f"Média de dias de empréstimo: {media_dias:.2f}")

sistema_biblioteca()
