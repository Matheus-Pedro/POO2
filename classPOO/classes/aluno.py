from classes.pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, cpf, idade, email, endereco, curso, turma, periodo):
        super().__init__(nome, cpf, idade, email, endereco)
        self.curso = curso
        self.turma = turma
        self.periodo = periodo

    def __str__(self):
        return f'{super().__str__()}Curso: {self.curso}\nTurma: {self.turma}\nPeriodo: {self.periodo}\n'
