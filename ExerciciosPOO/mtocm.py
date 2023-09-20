# Faça um Programa que converta metros para centímetros.

def mtocm(metros):
    centimetros = metros * 100
    
    if centimetros == 1:
        return f'{metros} metros é {centimetros} centímetro.'
    elif metros == 1:
        return f'{metros} metro são {centimetros} centímetros.'
    else: 
        return f'{metros} metros são {centimetros} centímetros.'
        
metros = float(input('Informe quantos metros você deseja converter: '))
print(mtocm(metros))
