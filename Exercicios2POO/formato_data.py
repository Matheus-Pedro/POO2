# Leia uma entrada e aplique um formato de data (programar)

data_input = input("Digite uma data no formato DD-MM-AAAA: ")
dia, mes,  ano = map(int, data_input.split('-'))

data = f'{dia}/{mes}/{ano}'
print(data)
