# Resolvendo Codigos em Python com ChatGPT

Aqui teremos resoluções de códigos em python usando o ChatGPT.

## 1 - Concatenando Dados

Descrição: Receberemos dois dados diferentes do usuário e concatená-lo-emos em uma única string.

```python
# Receber duas strings diferentes e concatena-los em uma única string

string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

resultado = string1 + " " + string2

print(f"String concatenada: {resultado}")
```

---

## 2 - Repetindo Textos

Descrição: Solicitaremos uma string e um número inteiro. Em seguida retornaremos a string repetida o número de vezes informado, com um espaço entre elas.

```python
# Solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado, com um espaço entre elas.

texto = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))

resultado = " ".join([texto] * numero)

print("Resultado:")
print(resultado)
```

---

## 3 - Operações Matemáticas

Descrição: Solicitaremos dois números com entrada e depois realizaremos uma das quatro operações básicas.

```python
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
```

---

## 4 - Verificando Números

Descrição: Receberemos um número inteiro como entrada e verificaremos se o número é par ou ímpar.

```python
# Receba um número inteiro e verifique se ele é par ou ímpar.

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
```

---

## 5 - Calculando Média

Descrição: Iremos calcular a média de três notas fornecidas pelo usuário

```python
# Calcular a média de três notas fornecidas na entrada do usuário

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"A média das notas é: {media:.2f}")
```

---

## 6 - Verificando Palíndromo

Descrição: Receberemos uma string e testaremos se ela é um palíndromo, invertendo ela e comparando-a.

```python
# Testar se a string é um palíndromo

texto = input("Digite uma palavra ou frase: ")

texto_formatado = texto.replace(" ", "").lower()

if texto_formatado == texto_formatado[::-1]:
    print(f'"{texto}" é um palíndromo.')
else:
    print(f'"{texto}" não é um palíndromo.')
```
