# Descrição: Implemente uma classe Carro com atributos para
# marca, modelo, ano e quilometragem. Inclua métodos para
# dirigir o carro, que aumenta a quilometragem, e outro método
# para exibir informações do carro.


class Carro:
    def __init__(self, marca, modelo, ano, quilometragem):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.quilometragem = quilometragem
    
    def acelera(self, quilometragem):
        if self.quilometragem == quilometragem:
            print('Mesma velocidade')
        else: 
            self.quilometragem += quilometragem
            print('aumentou')

    def exibir(self):
        print(f'Marca {self.marca}')
        print(f'Modelo {self.modelo}')
        print(f'Ano {self.ano}')
        print(f'Quilometragem {self.quilometragem}')


carro1 = Carro('Volks', 'UP', 2020, 10)

carro1.exibir()

carro1.acelera(200)

carro1.exibir()