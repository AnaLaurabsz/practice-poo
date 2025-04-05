# Crie uma classe Circulo com um atributo privado raio. Use a
# propriedade property para criar getters e setters para o raio.
# Além disso, adicione um método de propriedade area que
# calcule e retorne a área do círculo (área = π * raio^2). Garanta
# que o raio não possa ser negativo.

class Circulo:
    def __init__(self, raio):
        self.raio = raio
        # self.raio.setter(raio)

    # @property
    @property
    def raio(self):
        return self.__raio
    
    @raio.setter
    def raio(self, raio):
        if raio < 0:
            print('Raio não pode ser negativo')
        else:
            self.__raio = raio

    @property
    def area(self):
        return 3.14 * self.__raio**2
    

circ = Circulo(4)

print(circ.raio)

print(circ.area)

circ.raio = 8

print(circ.raio)

circ.raio = -5
print(circ.raio)

print(circ.area)