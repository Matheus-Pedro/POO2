class Pagamento:
    def __init__(self, forma_pagamento, sacador, sacado, data_hdma, valor): 
        #sacado -> devedor/Quem paga
        #sacador -> emitente/Quem recebe
        #data hdma -> hora, dia, mês e ano
        self.forma_pagamento = forma_pagamento
        self.sacador = sacador
        self.sacado = sacado
        self.data_hdma = data_hdma
        self.valor = valor

    def __str__(self):
        return f'\nForma de pagamento: {self.forma_pagamento}\nEmitente/Sacador: {self.sacador}\nDevedor/Sacado: {self.sacado}\nData(Hora, dia mês e ano): {self.data_hdma}\nValor: {self.valor}\n'