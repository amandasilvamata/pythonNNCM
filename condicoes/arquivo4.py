# calculadora 4 operações

numero1 = int(input("Escolha um número "))
numero2 = int(input("Escolha outro número "))
operacao = str(input("Qual operação você deseja fazer? \n +: soma \n -: subtração \n *: multiplicação \n /: divisão \n"))
resultado = 0

if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    resultado = numero1 / numero2
else:
    print("Opção inválida")

print(f"O resultado da operação {operacao} é de {numero1} {operacao} {numero2} = {resultado}")
