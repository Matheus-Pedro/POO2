from classes.pessoa import Pessoa
from classes.aluno import Aluno
from classes.funcionario import Funcionario
from classes.produto import Produto
from classes.veiculo import Veiculo
from classes.conta_a_pagar import ContaAPagar 
from classes.computador import Computador
from classes.smartphone import Smartphone
from classes.eletrodomestico import Eletrodomestico
from classes.pagamento import Pagamento #Importou todas as classes

#if (Pessoa.__name__ == '__main__'):

p1 = Pessoa('Matheus Pedro', 12345678901, 16, 'matheuscapriolipedro@gmail.com', 'Rua Antônio Chemin, 28, São Gabriel')#Nessas linhas abaixo, os Objetos são criados, definindo os valores dos atributos
f1 = Funcionario('Matheus', 12345678901, 16, 'matheuscapriolipedro@gmail.com', 'Rua Antônio Chemin, 28, São Gabriel', 1200.00, 'Desenvolvedor', 122, 'TI')
a1 = Aluno('Matheus Pedro', 12345678901, 16, 'matheuscaprolipedro@gmail.com', 'Rua Antônio Chemin, 28, São Gabriel', 'Informática', 2022, 2)
pr1 = Produto('ESP32', 12.50, 69.00, 110, 10)
v1 = Veiculo('Audi', 'TT', '2.5', 400, 3.7, 2020, 60_000, 'Cupê', 'Automático', 'Gasolina')
cp1 = ContaAPagar('Matheus Pedro', 'Banco do Brasil', 1_000, 10092023)
c1 = Computador(3.5, 8, 165, 'Windows', 3000.50)
s1 = Smartphone('Preto', 2023, '14 Pro Max', 'iPhone', 9_500.00)
e1 = Eletrodomestico('Aspirador de Pó', 'Limpar a sala', 'Smart 1300W ABS03 220V', 'Electrolux', 390.00)
pa1 = Pagamento('Pix', 'Ronan', 'Matheus', 5072007, 1_000.00) #Definiu todos os objetos 

print(p1)
print(f1)
print(a1)
print(pr1)
print(v1)
print(cp1)
print(c1)
print(s1)
print(e1)
print(pa1)