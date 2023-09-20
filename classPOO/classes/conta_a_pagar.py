class ContaAPagar:
    def __init__(self, nome, descricao, valor, data_vencimento):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.data_vencimento = data_vencimento 

    def __str__(self):
        return f'\nNome: {self.nome}\nDescrição: {self.descricao}\nValor: {self.valor}\nData de vencimento: {self.data_vencimento}\n'