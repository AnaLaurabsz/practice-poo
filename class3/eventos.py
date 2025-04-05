# Implemente uma classe Evento com atributos para
# nome do evento, data e número de participantes. Adicione
# métodos para alterar a data do evento e outro para exibir as
# informações do evento.

class Evento:
    def __init__(self, nome, data, num_partic):
        self.nome = nome
        self.data = data
        self.num_partic = num_partic

    def alterar_data(self, nova_data):
        if self.data == nova_data:
            print('Não foi possível alterar a data')
        else: 
            self.data = nova_data

    def exibir(self):
        print(f'Nome {self.nome}')
        print(f'Data {self.data}')
        print(f'Num participantes {self.num_partic:.3f}')


event1 = Evento('Ready To be Tour', '07/02/24', 25.000)

event1.exibir()

event1.alterar_data('06/02/24')

event1.exibir()