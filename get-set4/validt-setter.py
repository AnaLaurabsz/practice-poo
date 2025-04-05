# Crie uma classe Pessoa com um atributo privado idade e um
# atributo público nome. Use um getter e um setter para idade, e
# adicione validação no setter para garantir que a idade não seja
# negativa. Se uma idade negativa for passada, defina a idade
# como 0 e imprima uma mensagem de aviso.


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        # self.__idade = idade 
        self.set_idade(idade)

    def get_idade(self):
        return self.__idade
    
    def set_idade(self, new_idade):
        if new_idade < 0:
            self.__idade = 0
            print(f'A idade não pode ser negativa, portanto a idade foi definida como: {self.__idade}')
        else:
            self.__idade = new_idade

    # def exibir(self):
    #     print(f'Nome: {self.nome}')
    #     print(f'Idade: {self.__idade}')


pessoa1 = Pessoa('Ana', 19)

print(pessoa1.get_idade())

pessoa1.set_idade(-30)

print(pessoa1.get_idade())

pessoa1.set_idade(20)

print(pessoa1.get_idade())
