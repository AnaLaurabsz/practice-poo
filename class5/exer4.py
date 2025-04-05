class Professor:
    def __init__(self, nome):
        self.nome = nome 
        self.disciplinas = []

    def vincular_disciplina(self, disciplinas):
        self.disciplinas.append(disciplinas)

    def exibir_disciplinas(self):
        for disciplina in self.disciplinas:
            print(disciplina.nome)

class Disciplina:
    def __init__(self, nome):
        self.nome = nome



disciplina1 = Disciplina('poo')

disciplina2 = Disciplina('abc')

# print(disciplina1.nome)

# print(disciplina2.nome)

prof = Professor('fulano' )
prof.vincular_disciplina(disciplina1)
prof.vincular_disciplina(disciplina2)

prof.exibir_disciplinas()

# associe uma discplina a um professor