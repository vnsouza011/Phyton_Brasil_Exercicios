# 15 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

# Obs.: Salário Bruto - Descontos = Salário Líquido.

ganho_hora = float(input("Digite o quanto ganha por hora: "))

horas_mes = float(input("horas trabalhadas por mês: "))

salario_bruto = ganho_hora * horas_mes
imposto_de_renda = (salario_bruto * 11)/100
contribuicao_previdenciaria = (salario_bruto * 8)/100
sindicato = (salario_bruto * 5)/100
descontos = imposto_de_renda + contribuicao_previdenciaria + sindicato
salario_liquido = salario_bruto - descontos


print("Salário Bruto: {:.2f}".format(salario_bruto))
print("Imposto de renda: {:.2f}".format(imposto_de_renda))
print("INSS: {:.2f}".format(contribuicao_previdenciaria))
print("Sindicato: {:.2f}".format(sindicato))
print("Salário líquido: {:.2f}".format(salario_liquido))
