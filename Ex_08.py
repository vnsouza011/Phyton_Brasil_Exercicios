# 08 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

ganho_hora = float(input("Digite o quando ganha por hora: "))

hora_trabalhada =float(input("Digite quantas horas trabalha por dia: "))

ganho_diario =  ganho_hora * hora_trabalhada
dias_do_mes = 30

salario_total = ganho_diario * dias_do_mes

print("obs: O calculo é feito sob 30 dias do mês")

print("O seu salário mensal é de: ", salario_total)