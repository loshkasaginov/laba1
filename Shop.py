class Shop(object):
    def __init__(self, cash=0, price=0, id=""):
        self.cash = cash
        self.price = price
        self.id=id
    def setShopParams(self, cash=0, price=0, id=""):
        self.cash = cash
        self.price = price
        self.id = id

    def getname(self):
        return self.id

    def printShopParams(self):
        print(f'денег в магазине:{self.cash}, стоимость товара:{self.price}')

    def getShopParams(self):
        return self.price, self.cash

    def acttoware(self, kol,  ware):
        self.cash += kol * self.price
        ware.acc(kol)

    def actfromBuyer(self, kol, money, ware):
        if money < kol* self.price:
            print('недостаточно денег')
            return False
        elif kol > ware.getWareParams():
            print('на складе недостаточно товара')
            return False
        else:

            return True, kol * self.price