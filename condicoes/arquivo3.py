# preço da passagem dependendo da distância

distancia = float(input("Digite a distância que irá percorrer em km "))


if distancia <= 200:
    valor = distancia * 0.5
else:
    valor = distancia * 0.45


print(f"O valor que precisará pagar será de R${valor:.2f}")
