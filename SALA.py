class Sala:
    def __init__(self, numero):
        self.numero = numero

class Edificio:
    def __init__(self):
        self.sala1 = Sala(1)
        self.sala2 = Sala(2)
        self.salas = []