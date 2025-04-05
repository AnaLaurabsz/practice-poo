class Motor:
    def __init__(self, cilindrada, potencia):
        self.cilindrada = cilindrada
        self.potencia = potencia

    def __str__(self):
        return f"Motor: {self.cilindrada}cc, {self.potencia}CV"

class Veiculo:
    def __init__(self, ano, preco, motor):
        self.ano = ano
        self.preco = preco
        self.motor = motor

class Carro(Veiculo):
    def __init__(self, ano, preco, motor, cor, modelo):
        super().__init__(ano, preco, motor)
        self.cor = cor
        self.modelo = modelo

    def exibir_dados(self):
        print(f"Ano de fabricação: {self.ano}")
        print(f"Preço: {self.preco}")
        print(f"Motor: {self.motor.cilindrada}cc, {self.motor.potencia}CV")
        print(f"Cor: {self.cor}")
        print(f"Modelo: {self.modelo}")

class Caminhao(Veiculo):
    def __init__(self, ano, preco, motor, comprimento):
        super().__init__(ano, preco, motor)
        self.comprimento = comprimento

    def exibir_dados(self):
        print(f"Ano de fabricação: {self.ano}")
        print(f"Preço: {self.preco}")
        print(f"Motor: {self.motor.cilindrada}cc, {self.motor.potencia}CV")
        print(f"Comprimento: {self.comprimento} metros")

# Testes
motor1 = Motor(1000, 500)
motor2 = Motor(8000, 900)
carro = Carro(2010, 20000, motor1, "branca", "gol")
caminhao = Caminhao(2015, 80000, motor2, 10)

carro.exibir_dados()
print()
caminhao.exibir_dados()