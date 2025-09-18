# A academia guarda os atletas em uma lista de dicionários, cada um com:
# nome, idade, modalidades (lista de esportes), treinos (dicionário com o nome do esporte como
# chave e a quantidade de treinos realizados como valor).
# Tarefas:
# 1. Crie uma função que calcule a média de idade dos atletas que praticam um esporte
# específico.
# 2. Crie uma função que, dado um atleta, informe qual esporte ele mais treinou.
# 3. Monte uma lista com os atletas que praticam mais de 2 modalidades e exiba seus
# nomes.

atletas = [
    {
        "nome": "Lucas",
        "idade": 25,
        "modalidades": ["natação", "corrida"],
        "treinos": {"natação": 10, "corrida": 5}
    },
    {
        "nome": "Mariana",
        "idade": 30,
        "modalidades": ["ciclismo", "corrida", "yoga"],
        "treinos": {"ciclismo": 8, "corrida": 12, "yoga": 4}
    },
    {
        "nome": "Pedro",
        "idade": 22,
        "modalidades": ["natação", "ciclismo", "corrida", "musculação"],
        "treinos": {"natação": 15, "ciclismo": 7, "corrida": 10, "musculação": 20}
    },
    {
        "nome": "Ana",
        "idade": 28,
        "modalidades": ["yoga"],
        "treinos": {"yoga": 25}
    },
    {
        "nome": "Carla",
        "idade": 35,
        "modalidades": ["musculação", "natação", "pilates"],
        "treinos": {"musculação": 30, "natação": 5, "pilates": 10}
    }
]

def media_idade():
    esporte = input('Digite o nome de um esporte:\n >> ').strip().lower()
    atletas_esporte = [atleta for atleta in atletas if esporte in [m.lower() for m in atleta["modalidades"]]]
    
    if not atletas_esporte:
        print(f'Nenhum atleta pratica o esporte "{esporte}".')
        return
    
    media = sum(atleta["idade"] for atleta in atletas_esporte) / len(atletas_esporte)
    print(f'Média de idade dos atletas que praticam "{esporte}": {media:.2f} anos')

def esporte_mais_treinado():
    nome_atleta = input('Digite o nome do atleta:\n >> ').strip().lower()
    atleta = next((a for a in atletas if a["nome"].lower() == nome_atleta), None)
    
    if not atleta:
        print(f'Atleta "{nome_atleta}" não encontrado.')
        return
    
    esporte_mais_treinado = max(atleta["treinos"], key=atleta["treinos"].get)
    quantidade_treinos = atleta["treinos"][esporte_mais_treinado]
    print(f'O esporte mais treinado por {atleta["nome"]} é "{esporte_mais_treinado}" com {quantidade_treinos} treinos.')

def atletas_multimodalidade():
    atletas_multimodal = [atleta["nome"] for atleta in atletas if len(atleta["modalidades"]) > 2]
    print("Atletas que praticam mais de 2 modalidades:", atletas_multimodal)

media_idade()
esporte_mais_treinado()
atletas_multimodalidade()
