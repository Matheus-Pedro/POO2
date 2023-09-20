class Veiculo: 
    def __init__(self, marca, nome, motor, cavalos, zero_cem, ano, km, carroceria, cambio, combustivel):
        self.marca = marca
        self.nome = nome
        self.motor = motor
        self.cavalos = cavalos
        self.zero_cem = zero_cem
        self.ano = ano
        self.km = km
        self.carroceria = carroceria
        self.cambio = cambio
        self.combustivel = combustivel

    def __str__(self):
        return f'\nMarca: {self.marca}\nNome: {self.nome}\nMotor: {self.motor}\nCavalos: {self.cavalos}\n0 a 100(seg.): {self.zero_cem}\nAno: {self.ano}\nKm: {self.km}\nCarroceria: {self.carroceria}\nCâmbio: {self.cambio}\nCombustível: {self.combustivel}\n'