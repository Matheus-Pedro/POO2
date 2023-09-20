class Pessoa:
    def __init__(self, nome, cpf, idade, email, endereco):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.email = email
        self.endereco = endereco

    def __str__(self):
        return f'\nNome: {self.nome}\nCPF: {self.cpf}\nIdade: {self.idade}\nEmail: {self.email}\nEndereço: {self.endereco}\n'