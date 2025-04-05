class Produto: 
    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
    
    def adicionar(self, qtd):
        if qtd > 0:
            self.add += qtd
    
    def remover(self, qtd):
        if qtd > 1:
            self.rem -= qtd
    
    def imprimi(self):
        print(f'Nome: {self.nome}')
        print(f'Preço: {self.preco}')
        print(f'Quantidade: {self.qtd}')
        
prod1 = Produto('Banana', 5, 19)

prod1.imprimi()
