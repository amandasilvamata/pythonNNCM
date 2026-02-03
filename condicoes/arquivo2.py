#um programa que calcule o valor de aumento do salario

salario = float(input("Digite o seu sálario: "))
base = float(1250)
aumento = 0
novoSal= 0


if salario > base :
    aumento = salario * 0.10
    novoSal = salario * 1.10
if salario < base :
    aumento = salario * 0.15
    novoSal = salario * 1.15

print(f"O seu antigo sálario era R${salario:.2f} e teve um aumento de R${aumento:.2f} ficando agora no valor de R${novoSal:.2f}")
