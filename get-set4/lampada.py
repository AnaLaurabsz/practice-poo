# Crie uma classe Lampada com um atributo privado estado
# (ligado/desligado). Implemente métodos getters e setters para o
# atributo estado. O setter deve aceitar apenas os valores
# "ligado" ou "desligado" e alterar o estado da lâmpada de
# acordo.


class Lampada:
    def __init__(self, estado = 'desligado'):
        # self.__estado = estado
        self.set_estado(estado)

    def get_estado(self):
        return self.__estado 
    
    def set_estado(self, new_estado):
        if new_estado in ['ligado', 'desligado']:
            self.__estado = new_estado
            print(f'A lâmpada está {self.__estado}')
        else:
            print('Estado inválido! Use "ligado" ou "desligado"')

lampada = Lampada()

print(lampada.get_estado())

lampada.set_estado('ligado')

print(lampada.get_estado())


