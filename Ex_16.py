#Faça um programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

print("***********************")
print("***** Tinturaria ******")
print("***********************")

area_pintada = float(input("Digite a area em m² que será pintada: "))

valor_lata = 80

quantidade_de_tinta = area_pintada / 3

latas = int(quantidade_de_tinta / 18)

if (quantidade_de_tinta % 18 != 0):
    latas += 1

print("É necessário comprar: {:.2f}".format(latas), "latas")
print("Valor total: {:.2f}".format(latas * valor_lata))
