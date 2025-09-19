# --- valor aluguel do carro ---

dias = int(input("Digite a quantidade de dias que você alugou o carro: "))
km = float(input("Digite quantos km você rodou com o carro: "))

pagamento = ((dias * 60) + (km * 0.15))

print("Você pagará R$%.2f pelo aluguel do carro" %(pagamento))
