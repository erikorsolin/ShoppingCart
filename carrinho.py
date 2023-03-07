class Carrinho:
    def __init__(self) -> None:
        self.__qtd_produtos = 0
        self.__preco_total = 0
        self.__produtos = dict()
    
    def AdicionarProduto(self, nome: str, preco: float) -> None:
        self.__produtos[nome] = preco
        self.__qtd_produtos += 1
        self.__preco_total += self.__produtos[nome]
        print('Produto Adicionado')
        

    def RemoverProduto(self, nome: str) -> None:
        if self.__verificar_produto(nome):
            self.__preco_total -= self.__produtos[nome]
            del self.__produtos[nome]
            print('Produto Removido')
            self.__qtd_produtos -= 1

        else:
           print('Produto não está no Carrinho')


    def __verificar_produto(self, nome: str) -> bool:
        if nome in self.__produtos.keys():
            return True
        else:
            return False

    
    def GetQuantidadeProdutos(self) -> int:
        return self.__qtd_produtos


    def GetPrecoTotal(self) -> float:
        return self.__preco_total
    
    
    def GetProdudos(self) -> dict:
        return self.__produtos