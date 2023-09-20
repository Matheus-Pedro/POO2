# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: Para homens: (72.7*h) - 58   Para mulheres: (62.1*h) - 44.7

gender = int(input('\tInforme seu genêro.\n[1] Mulher\n[2] Homem\n'))
h = float(input('Informe sua altura: '))

match gender:
    case 1:
        peso_ideal = (62.1*h)-44.7
        print(f'Seu peso ideal seria: {peso_ideal}')
    case 2: 
        peso_ideal = (72.7*h)-58
        print(f'Seu peso ideal seria: {peso_ideal :.2f}')
    case _:
        print(f'Genêro informado incorretamente.')
