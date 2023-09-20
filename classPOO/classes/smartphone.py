class Smartphone:
    def __init__(self, cor, ano, modelo, marca, preco):
        self.cor = cor
        self.ano = ano
        self.modelo = modelo
        self.marca = marca
        self.preco = preco

    def __str__(self):
        return f'\nCor do Smartphone: {self.cor}\nAno de lançamento: {self.ano}\nModelo do Smartphone: {self.modelo}\nMarca: {self.marca}\nPreço: {self.preco}\n'