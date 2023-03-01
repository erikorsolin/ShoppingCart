class Carrinho:
    def __init__(self, nome_usuario: str):
        self.__nome_usuario = nome_usuario
        self.__qtd_produtos = 0
        self.__preco_total = 0
        self.__produtos = dict()
    
    def AdicionarProduto(self, nome: str, preco: float) -> str:
        self.produtos[nome] = preco
        self.qtd_produtos += 1
        self.preco_total += self.produtos[nome]
        r = 'Produto Adicionado'
        return r



    def RemoverProduto(self, nome: str) -> str:
        r = ''
        if nome in self.produtos.keys():
            self.preco_total -= self.produtos[nome]
            del self.produtos[nome]
            r = 'Produto Removido'
            self.qtd_produtos -= 1         
        else:
            r = 'Produto não Está no Carrinho'

        return r
    

    
    def GetQuantidadeProdutos(self) -> int:
        return self.__qtd_produtos


    def GetPrecoTotal(self) -> float:
        return self.__preco_total
    
    
    def GetProdudos(self) -> dict:
        return self.__produtos

    
    def GetNomeUsuario(self) -> str:
        return self.__nome_usuario