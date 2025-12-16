# Solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite a opção: ")

if opcao == "1":
    resultado = numero1 + numero2
    print(f"Resultado da soma: {resultado}")

elif opcao == "2":
    resultado = numero1 - numero2
    print(f"Resultado da subtração: {resultado}")

elif opcao == "3":
    resultado = numero1 * numero2
    print(f"Resultado da multiplicação: {resultado}")

elif opcao == "4":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"Resultado da divisão: {resultado}")
    else:
        print("Erro: divisão por zero não é permitida.")

else:
    print("Opção inválida!")
