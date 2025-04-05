# Crie a classe Animal com os atributos nome, cor e
# numero_patas. Crie também o método exibir_dados, que
# imprime na tela os dados do animal (nome, cor e
# numero_patas).

# Crie a classe Cachorro que herda da classe Animal e que
# possui como atributo adicional a raça do cachorro. Crie também
# o método exibir_dados, que imprime na tela os dados do
# cachorro (nome, cor, numero_patas e raca)


class Animal:
    def __init__(self, nome, cor, num_patas):
        self.nome = nome
        self.cor = cor
        self.num_patas = num_patas

    def exibir_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Cor: {self.cor}')
        print(f'Numero de patas: {self.num_patas}')


class Cachorro(Animal):
    def __init__(self, nome, cor, num_patas, raca):
        super().__init__(nome, cor, num_patas)
        self.raca = raca
        



































# class Animal:
#     def __init__(self, nome, cor, numero_patas):
#         self.nome = nome
#         self.cor = cor
#         self.numero_patas = numero_patas

#     def exibir_dados(self):
#         print(f'Nome: {self.nome}')
#         print(f'Cor: {self.cor}')
#         print(f'Numero de patas: {self.numero_patas}')


# class Cachorro(Animal):
#     def __init__(self, nome, cor, numero_patas, raca):
#         super().__init__(nome, cor, numero_patas)
#         self.raca = raca

#     def exibir_dados(self):
#         print(f'Nome: {self.nome}')
#         print(f'Cor: {self.cor}')
#         print(f'Numero de patas: {self.numero_patas}')
#         print(f'Raça: {self.raca}')

# animal = Animal("Passarinho", "Azul", 2)
# animal.exibir_dados()


# catioro = Cachorro("Rex", "Marrom", 4, "Vira lata")
# catioro.exibir_dados()