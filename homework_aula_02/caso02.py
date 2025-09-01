import math

# Caso2: Distâncias em Km
# 1. Receba as distâncias percorridas em 6 viagens e armazene em uma lista.
# 2. Calcule a distância total percorrida.
# 3. Mostre a maior e a menor distância.
# 4. Calcule a média das distâncias arredondada para cima (use math.ceil).

def registrar_distancias():
    distancias = []
    for i in range(1, 7):
        d = float(input(f"Digite a distância da viagem {i} em km: "))
        distancias.append(d)
    return distancias

def distancia_total(distancias):
    return sum(distancias)

def maior_menor_distancia(distancias):
    return max(distancias), min(distancias)

def media_arredondada(distancias):
    media = sum(distancias) / len(distancias)
    return math.ceil(media)

distancias = registrar_distancias()
total = distancia_total(distancias)
maior, menor = maior_menor_distancia(distancias)
media = media_arredondada(distancias)

print(f"\nDistâncias registradas: {distancias}")
print(f"Distância total percorrida: {total} km")
print(f"Maior distância: {maior} km")
print(f"Menor distância: {menor} km")
print(f"Média das distâncias (arredondada para cima): {media} km")
