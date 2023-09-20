class Computador:
    def __init__(self, GHz_processador, memoria_RAM, armazenamento, sistema_operacional, preco):
        self.GHz_processador = GHz_processador  
        self.memoria_RAM = memoria_RAM
        self.armazenamento = armazenamento
        self.sistema_operacional = sistema_operacional
        self.preco = preco

    def __str__(self):
        return f'\nGhz do processador: {self.GHz_processador}\nQuantidade de memória RAM: {self.memoria_RAM}\nEspaço no armazenamento (Em GB): {self.armazenamento}\nSistema operacional: {self.sistema_operacional}\nPreço do computador: {self.preco}\n'