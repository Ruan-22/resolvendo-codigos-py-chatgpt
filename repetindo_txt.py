# Solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado, com um espaço entre elas.

texto = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))

resultado = " ".join([texto] * numero)

print("Resultado:")
print(resultado)
