# 14 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes)
# e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.

peso_limite = 50.00
multa = 4.00
print("Limite de peso: ", peso_limite)

peso_peixe = float(input("Digite o peso do peixe: "))

if(peso_peixe <= peso_limite):
    print("Esta dentro do peso permitido !")

elif(peso_peixe > peso_limite):
    excesso = peso_peixe - 50
    valor_da_multa =  excesso * multa
    print("O Excesso foi de: ", excesso, ". O valor da multa é de: ", valor_da_multa, " Reais")


