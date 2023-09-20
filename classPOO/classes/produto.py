class Produto:
    def __init__(self, nome, preco_compra, preco_venda, quantidade_estoque, garantia):
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.quantidade_estoque = quantidade_estoque
        self.garantia = garantia

    def __str__(self):
        return f'\nNome: {self.nome}\nPreço de Compra: {self.preco_compra}\nPreço de Venda: {self.preco_venda}\nQuantidade no Estoque: {self.quantidade_estoque}\nTempo de garantia(dias): {self.garantia}'