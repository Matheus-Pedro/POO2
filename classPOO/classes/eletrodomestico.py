class Eletrodomestico:
    def __init__(self, nome, utilidade, modelo, marca, preco):
        self.nome = nome
        self.utilidade = utilidade
        self.modelo = modelo
        self.marca = marca
        self.preco = preco

    def __str__(self):
        return f'\nNome do eletrodoméstico: {self.nome}\nQual a função: {self.utilidade}\nModelo do {self.nome}: {self.modelo}\nMarca: {self.marca}\nPreço: {self.preco}\n'