# Crie uma classe ContaBancaria que tenha um atributo
# privado saldo e um atributo público titular. Inicialize ambos
# os atributos no método __init__. Em seguida, crie um método
# para depositar dinheiro e outro para exibir o saldo, garantindo
# que o saldo não possa ser acessado diretamente de fora da
# classe.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, deposito):
        if deposito < 0:
            print('Não foi possível realizar o depósito')
        else:
            self.__saldo += deposito

    def exibir_saldo(self):
        print(f'Seu saldo é: {self.__saldo}')


conta = ContaBancaria('Laura', 10)

conta.exibir_saldo()

conta.depositar(5)

conta.exibir_saldo()

conta.depositar(-5)

conta.exibir_saldo()

conta.depositar(-5)


# class Conta:
#     def __init__(self, titular, saldo):
#         self.titular = titular
#         self.__saldo = saldo

#     def deposito(self, new_saldo):
#         if self.__saldo > 0:
#             self.__saldo += new_saldo

#     def exibe_saldo(self):
#         print(f'Saldo = {self.__saldo}')

# conta1 = Conta('Ana', 200)

# conta1.exibe_saldo()

# conta1.deposito(1000)

# conta1.exibe_saldo()