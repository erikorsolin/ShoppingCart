class Carrinho:
    def __init__(self, nome_usuario):
        self.nome_usuario = nome_usuario
        self.qtd_produtos = 0
        self.preco_total = 0
        self.produtos = dict()

    def AdicionarProduto(self, nome, preco):
        self.produtos[nome] = preco
        self.qtd_produtos += 1
        self.preco_total += self.produtos[nome]

    def RemoverProduto(self, nome):
        r = ''
        if nome in self.produtos.keys():
            self.preco_total -= self.produtos[nome]
            del self.produtos[nome]
            r = 'Produto Removido'
            self.qtd_produtos -= 1         
        else:
            r = 'Produto não Está no Carrinho'

        return r
    
    
    def GetQuantidadeProdutos(self):
        return self.qtd_produtos
    
    
    def GetPrecoTotal(self):
        return self.preco_total
    
    
    def GetProdudos(self):
        return self.produtos

    
    def GetNomeUsuario(self):
        return self.nome_usuario