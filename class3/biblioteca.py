# Descrição: Desenvolva uma classe Livro com atributos para título,
# autor, ano de publicação e disponibilidade. Adicione métodos
# para emprestar e devolver o livro, alterando seu status de
# disponibilidade.

class Livro:
    def __init__(self, titulo, autor, ano_publi, disponibilidade = True):
        self.titulo = titulo
        self.autor = autor
        self.ano_publi = ano_publi
        self.disponibilidade = disponibilidade

    def emprestar(self):
        if self.disponibilidade:
            self.disponibilidade = False
            print('Emprestado')
        else:
            print('Livro não disponível')

    def devolver(self):
        if self.disponibilidade == False:
            self.disponibilidade = True
            print('Devolvido')
        else:
            print('Não foi emprestado')

livro1 = Livro('Estatística', 'David Salsburg', 2017)

# print(livro1)

# livro1.emprestar()
livro1.devolver()