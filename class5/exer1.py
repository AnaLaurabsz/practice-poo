# Crie a classe Pessoa com os atributos identificador e nome.
# Crie a classe PessoaJuridica que herda da classe Pessoa e
# acrescenta o atributo CNPJ.
# Crie a classe PessoaFisica que herda da classe Pessoa e
# acrescenta os atributos RG e CPF.

class Pessoa:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome 

class PessoaFisica(Pessoa):
    def __init__(self, id, nome, cpf, rg):
        super().__init__(id, nome)
        self.cpf = cpf
        self.rg = rg

class PessoaJuridica(Pessoa):
    def __init__(self, id, nome, cnpj):
        super().__init__(id, nome)
        self.cpf = cnpj


#  O super herda os atributos da classe mãe 