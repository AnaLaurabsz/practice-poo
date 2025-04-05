# Modifique a classe Lampada do Exercício 2 para usar o
# decorator property. Reescreva os getters e setters usando a
# sintaxe de property. Certifique-se de que a funcionalidade de
# ligar e desligar a lâmpada permaneça a mesma.


class Lampada:
    def __init__(self, estado ='desligado'):
        # self.set_estado(estado)
        self.estado = estado

    @property
    # @estado.getter
    def estado(self):
        return self.__estado 
    
    @estado.setter 
    def estado(self, new_estado):
        if new_estado in ['desligado', 'ligado']:
            self.__estado = new_estado
        else:
            print('Estado inválido! Use "ligado" ou "desligado"')
    
lampada = Lampada()

print(lampada.estado)

lampada.estado = 'abc'

print(lampada.estado)

lampada.estado = 'ligado'

print(lampada.estado)
