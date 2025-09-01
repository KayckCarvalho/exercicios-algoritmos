# Caso6: Sistema de Biblioteca
# Uma biblioteca mantém uma lista de livros emprestados, onde cada item é representado por
# [titulo, usuario, dias_emprestado].
# Exemplo:
# [
#  ["Dom Casmurro", "Ana", 5],
#  ["1984", "Carlos", 12],
#  ["O Hobbit", "Marina", 3]
# ]
# O sistema precisa:
# 1. Listar apenas os livros que estão emprestados há mais de 7 dias.
# 2. Encontrar o livro emprestado há mais tempo.
# 3. Gerar uma lista apenas com os nomes dos usuários que têm livros emprestados.
# 4. Calcular a média de dias de empréstimo.

def livros_acima_7_dias(emprestimos):
    return [livro for livro in emprestimos if livro[2] > 7]

def livro_mais_tempo(emprestimos):
    return max(emprestimos, key=lambda x: x[2])

def usuarios_com_emprestimos(emprestimos):
    return list({livro[1] for livro in emprestimos})  
def media_dias_emprestimo(emprestimos):
    total_dias = sum(livro[2] for livro in emprestimos)
    return total_dias / len(emprestimos) if emprestimos else 0

emprestimos = [
    ["Dom Casmurro", "Ana", 5],
    ["1984", "Carlos", 12],
    ["O Hobbit", "Marina", 3],
    ["O Senhor dos Anéis", "João", 10]
]

livros_7_dias = livros_acima_7_dias(emprestimos)
livro_mais = livro_mais_tempo(emprestimos)
usuarios = usuarios_com_emprestimos(emprestimos)
media_dias = media_dias_emprestimo(emprestimos)

print("Livros emprestados há mais de 7 dias:", livros_7_dias)
print("Livro emprestado há mais tempo:", livro_mais)
print("Usuários com livros emprestados:", usuarios)
print("Média de dias de empréstimo:", round(media_dias, 2))
