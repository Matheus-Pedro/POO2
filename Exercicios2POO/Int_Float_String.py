# Leia uma entrada e transforme em int, float e string
# Leia uma entrada, converta para int, float e string e avise se houve perda de precisão

var_input = input('Informe algo: ')

var_str = str(var_input)

try:
    var_int = int(var_input)
except:
    var_int = 'Não é um número inteiro válido'

try:
    var_float = float(var_input)
except:
    var_float = 'Não é um número real válido'

print(f'''String: '{var_str}'
Integer: {var_int}
Float: {var_float}''')
