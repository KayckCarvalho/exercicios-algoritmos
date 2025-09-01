# Uma professora precisa registrar a presença dos alunos durante a semana.
# • Cada dia da semana terá uma lista com os nomes dos presentes.
# • No final, ela precisa:
# 1. Saber quais alunos estiveram presentes todos os dias.
# 2. Saber quais alunos faltaram em pelo menos um dia.
# 3. Saber o número total de presenças por aluno.

def registrar_presencas(presencas_semana):
    todos_alunos = set()
    for dia in presencas_semana:
        todos_alunos.update(presencas_semana[dia])
    presentes_todos_dias = set(presencas_semana[list(presencas_semana.keys())[0]])
    for dia in presencas_semana.values():
        presentes_todos_dias.intersection_update(dia)
    faltaram_ao_menos_um_dia = todos_alunos - presentes_todos_dias 
    total_presencas = {aluno: 0 for aluno in todos_alunos}
    for dia in presencas_semana.values():
        for aluno in dia:
            total_presencas[aluno] += 1

    return presentes_todos_dias, faltaram_ao_menos_um_dia, total_presencas

# Exemplo de uso
presencas_semana = {
    "Segunda": ["Ana", "Bruno", "Carlos"],
    "Terca": ["Ana", "Bruno"],
    "Quarta": ["Ana", "Bruno", "Carlos"],
    "Quinta": ["Ana", "Bruno", "Carlos"],
    "Sexta": ["Ana", "Bruno"]
}

presentes_todos, faltaram, total = registrar_presencas(presencas_semana)

print("Alunos presentes todos os dias:", presentes_todos)
print("Alunos que faltaram em pelo menos um dia:", faltaram)
print("Número total de presenças por aluno:", total)
