# exercício multa por km/h

velocidade = int(input("Digite a velocidade do seu carro em km/h: "))



if velocidade > 80:
    valor = float((velocidade - 80) * 5)
    print("Você foi MULTADO por ultrapassar o limite de velocidade de 80 km/h o valor da sua multa é: R$ %.2f" %(valor))
