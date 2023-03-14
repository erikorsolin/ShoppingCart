class Cart:
    def __init__(self) -> None:
        self.__count_products = 0
        self.__total_price = 0
        self.__products = dict()
    
    def add_product(self, name: str, price: float) -> None:
        self.__products[name] = price
        self.__count_products += 1
        self.__total_price += self.__products[name]
        print('product added')
        

    def remove_product(self, name: str) -> None:
        if  self.__verifyproduct(name):
            self.__total_price -= self.__products[name]
            del self.__products[name]
            print('product removed')
            self.__count_products -= 1

        else:
           print('product is not in cart')


    def __verifyproduct(self, name: str) -> bool:
        if name in self.__products.keys():
            return True
        else:
            return False

    
    def get_count_products(self) -> int:
        return self.__count_products


    def get_price_products(self) -> float:
        return self.__total_price
    
    
    def get_products(self) -> dict:
        return self.__products