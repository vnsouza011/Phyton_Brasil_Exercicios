# 09 -Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
# C = (5 * (F-32) / 9).
print("Conversor de temperatura Farenhenit para celsius")

graus_farenheint = float(input("Digite a temperatura farenheint: "))

graus_celsius = (5 * (graus_farenheint - 32) / 9)

print("a conversão de: ", graus_farenheint,"ºF  para ", graus_celsius,"ºC")