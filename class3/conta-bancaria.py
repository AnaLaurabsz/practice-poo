# Descrição: Crie uma classe ContaBancaria com atributos para o
# titular da conta, número da conta e saldo. Inclua métodos para
# depositar e sacar dinheiro, além de um método para exibir as
# informações da conta.

class ContaBancaria:
    def __init__(self, titular, num_conta, saldo):
        self.titular = titular
        self.num_conta = num_conta
        self.saldo = saldo

    def depositar(self, deposito):
        if deposito >= 1:
            self.saldo += deposito
        else:
            print('Não foi possível realizar o depósito')

    def sacar(self, saque):
        if self.saldo < 0 or saque > self.saldo:
            print('Não foi possível realizar o saque')
        else:
            self.saldo -= saque

    def exibir(self):
        print(f'Titular: {self.titular}')
        print(f'Número da conta: {self.num_conta}')
        print(f'Saldo: {self.saldo}')


conta1 = ContaBancaria('Ana Laura', 1234, 10)

conta1.exibir()

conta1.sacar(5)

conta1.exibir()

conta1.sacar(12)

conta1.exibir()

conta1.depositar(45)

conta1.exibir()

conta1.sacar(40)

conta1.exibir()


conta1.depositar(-100)

conta1.exibir()