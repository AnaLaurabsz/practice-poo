# Descrição: Implemente uma classe Produto com atributos para
# nome, preço e quantidade em estoque. Adicione métodos para
# adicionar e remover produtos do estoque, e um método para
# imprimir as informações do produto.

class Produto:
    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd

    def adicionar(self, qtd):
        if qtd > 0:
            self.qtd += qtd
        else:
            print('Quantidade inválida')
    
    def remover(self, qtd):
        if qtd > 0 and self.qtd >= qtd:
            self.qtd -= qtd
        else:
            print('Quantidade inválida ao remover')

    def exibir(self):
        print(f'Nome: {self.nome}')
        print(f'Preço: {self.preco}')
        print(f'Quantidade: {self.qtd}')


prd1 = Produto('Mouse', 56, 12)

prd2 = Produto('Monitor', 500, 5)

prd1.adicionar(8)


prd2.remover(5)


prd1.exibir()

prd2.remover(1)
prd2.adicionar(1)
prd2.exibir()