# 11 -Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

num01 = int(input("Digite o primeiro número inteiro: "))

num02 = int(input("Digite o segundo número inteiro: "))

num03 = float(input("Digite o númro real: "))


resposta_01 = (num01 * 2) + (num02/2)

resposta_02 = (num01 * 3) + num03

resposta_03 = num03 * num03 * num03


print("o produto do dobro do primeiro com metade do segundo: ", resposta_01)

print("a soma do triplo do primeiro com o terceiro: ", resposta_02)

print("o terceiro elevado ao cubo: ", resposta_03)

