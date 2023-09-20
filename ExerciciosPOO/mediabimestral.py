# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

aux = 0
for i in range (4):
    bimestre = float(input(f'Informe a nota do {i+1}° Bimestre: '))
    aux += bimestre
    print(aux)
aux = aux/4

print(f'Média anual do aluno: {aux}')