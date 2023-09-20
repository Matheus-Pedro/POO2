from classes.pessoa import Pessoa

class Funcionario(Pessoa): #Cria Classe funcionário herdando atributos e 'dunders' da classe pessoa 
    def __init__(self, nome, cpf, idade, email, endereco, salario, profissao, duracao_contrato, setor):
        super().__init__(nome, cpf, idade, email, endereco) #atributos herdados da classe pessoa
        self.salario = salario
        self.profissao = profissao
        self.duracao_contrato = duracao_contrato
        self.setor = setor

    def __str__(self):
        return f'{super().__str__()}Salário: {self.salario}\nProfissão: {self.profissao}\nDuração do contrato(Dias): {self.duracao_contrato}\nSetor: {self.setor}\n'