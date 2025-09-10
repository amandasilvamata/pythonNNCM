item = float(input("Digite o valor do produto: "))
desconto = float(input("Digite o desconto: "))

novoValor = (item - ((desconto/100) * item))

print(novoValor)
