# Crie um programa que:
# 1. Receba as temperaturas de 7 dias e armazene em uma lista.
# 2. Mostre a média das temperaturas da semana.
# 3. Informe o dia mais quente e o dia mais frio.
# 4. Mostre quantos dias ficaram acima da média.

temperaturas = []
for i in range(1, 8):
    temp = float(input(f'digite a temperadura do dia {i}: \n >>'))
    temperaturas.append(temp)

def media_temp(temperaturas):
    resultado = 0
    for n in temperaturas:
        resultado += n
    return resultado/len(temperaturas)

def temp_acima_media(media, temperaturas):
    acima_media = 0
    for n in temperaturas:
        if n > media:
            acima_media += 1
    return acima_media


media = media_temp(temperaturas)
Menor = max(temperaturas)
maior = min(temperaturas)
acima = temp_acima_media(media, temperaturas)

print(f'A maior temperatura foi de {maior}°C')
print(f'A menor temperatura foi de {Menor}°C')
print(f'A media das temperaturas foi de {media}°C')
print(f'Temperaturas acima da media: {acima}')


