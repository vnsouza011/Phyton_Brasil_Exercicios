# 07 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado_quad = float(input("Digite o tamanho do lado do quadrado em metros: "))

quad_area = lado_quad * lado_quad
dobro_area = quad_area * quad_area
print(" O dobro da area de: ", quad_area, "m² é de: ",dobro_area,"m²")

