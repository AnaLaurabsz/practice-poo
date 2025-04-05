# Descrição: Crie uma classe Pessoa com atributos para nome,
# idade e endereço. Inclua métodos para alterar o endereço e
# outro para exibir todas as informações da pessoa.

class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def alterar(self, altera):
        if self.endereco == altera:
            print("Esse é seu endereço atual")
        else:
            self.endereco = altera
    def exibir(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Endereço: {self.endereco}')

p1 = Pessoa('Ana', 18, 'Rua Lourenço')

p1.exibir()
p1.alterar('Rua Lourenço')

p1.exibir()