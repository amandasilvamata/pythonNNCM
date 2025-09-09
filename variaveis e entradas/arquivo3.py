salario = float(input("Digite o valor do seu salário: "))
aumento = float(input("Digite a porcentagem de aumento do salário: "))

salarioNovo = (salario * (aumento/100 + 1))

print("O valor do novo salário é R$%.2f" % (salarioNovo))
