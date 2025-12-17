# Testar se a string é um palíndromo

texto = input("Digite uma palavra ou frase: ")

texto_formatado = texto.replace(" ", "").lower()

if texto_formatado == texto_formatado[::-1]:
    print(f'"{texto}" é um palíndromo.')
else:
    print(f'"{texto}" não é um palíndromo.')
