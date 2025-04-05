class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.set_idade(idade)

    def get_idade(self):
        return self.idade

    def set_idade(self, idade):
        while idade < 18:
            idade = int(input('Digite uma idade válida'))
        self.idade = idade

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.set_salario(salario)

    def get_salario(self):
        return self.__salario
    
    def set_salario(self, salario):
        self.__salario = salario
            
    def calcula_salario_anual(self):
        return self.__salario * 12


class Departamento:
    def __init__(self):
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def calcular_total_salarios(self):
        total_salarios = 0
        for funcionario in self.funcionarios:
            total_salarios += funcionario.calcula_salario_anual()
            return (f'O departamento gasta R${total_salarios} de salario por ano')
        
    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(f'O funcionário {funcionario.nome} recebe {funcionario.calcula_salario_anual()} por ano')



# func1 = Funcionario('Ana', 19, 600)

# func2 = Funcionario('Laura', 25, 800)

# func3 = Funcionario('Sandra', 29, 300)

# dep = Departamento()

# dep.adicionar_funcionario(func1)
# dep.adicionar_funcionario(func2)
# dep.adicionar_funcionario(func3)



# print(func1.calcula_salario_anual())



class Exemplo:
    def __init__(self):
        self.publico = "Eu sou público"
        self._protegido = "Eu sou protegido"
        self.__privado = "Eu sou privado"

    def metodo_publico(self):
        return "Este é um método público"

    def _metodo_protegido(self):
        return "Este é um método protegido"

    def __metodo_privado(self):
        return "Este é um método privado"

# Usando a classe
obj = Exemplo()

print(obj.publico)          # Acesso ao atributo público
print(obj._protegido)       # Acesso ao atributo protegido (possível, mas contra a convenção)
# print(obj.__privado)      # Isso resultará em erro, mas ainda é possível acessar de forma "indireta"
print(obj._Exemplo__privado)# Com name mangling aplicado

# print(obj.metodo_publico())
# print(obj._metodo_protegido())
# # print(obj.__metodo_privado())  # Isso também resultará em erro
# print(obj._Exemplo__metodo_privado()) # Com name mangling aplicado