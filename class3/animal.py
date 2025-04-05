# Descrição: Desenvolva uma classe AnimalDeEstimacao com
# atributos para nome, espécie e idade. Inclua métodos para
# alterar a idade do animal e outro para exibir as informações do
# animal.

class AnimalDeEstimacao:
    def __init__(self, nome, especie, idade):
        self.nome = nome
        self.especie = especie
        self.idade = idade

    def alterar_idade(self, idade):
        if self.idade == idade:
            print('Não foi possível alterar a idade')
        else:
            self.idade = idade 

    def exibir(self):
        print(f'Nome {self.nome}')
        print(f'Espécie {self.especie}')
        print(f'Idade {self.idade}')


pet1 = AnimalDeEstimacao('Pipo', 'Felino', 2)

pet1.exibir()

pet1.alterar_idade(5)

pet1.exibir()