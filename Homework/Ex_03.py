
notas = [7, 5, 8, 10, 2]
soma = 0
elementos = 0

for i in notas:
    soma += i
    elementos += 1
    
media = soma/elementos
print(f'media: {media}')

print(f'Maior nota: {max(notas)}')

acima_media = 0
for n in notas:
    if n >= 7:
        acima_media += 1
percentual = (acima_media/elementos)*100

print(f'Alunos acima da media: {percentual:.2f}%')