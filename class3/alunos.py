# Descrição: Crie uma classe Aluno com atributos para nome,
# matrícula e curso. Adicione métodos para mudar o curso do
# aluno e outro para exibir as informações do aluno.

class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

    def mudar_curso(self, curso):
        if self.curso == curso:
            print('Não foi possível mudar de curso')
        else:
            self.curso = curso
            print('Vc mudou de curso!')
            print(f'Vc mudou para o curso de {self.curso}')

    def exibir(self):
        print(f'Nome {self.nome}')
        print(f'Matrícula {self.matricula}')
        print(f'Curso {self.curso}')


aluno1 = Aluno('Ana', 2402680, 'ADS')

aluno1.exibir()

aluno1.mudar_curso('SI')

aluno1.exibir()