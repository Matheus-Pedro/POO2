# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

horas_trabalhadas = int(input('Informe quantas horas trabalhadas no mês: '))
ganho_por_hora = int(input('Informe o ganho por hora: '))

salario_mensal = horas_trabalhadas * ganho_por_hora
print(f'Seu salário mensal é: {salario_mensal}')
