from Buyer import Buyer
from Shop import Shop
from Warehouse import Warehouse



def main():
    warehouses={}
    shops={}
    buyers={}
    print(
        f" если вы хотите увидеть список команд, введите \help\n "
        f"если вы хотите добавить покупателя, введите 1. \n"
        f" есля вы хотите добавить магазин, введите 2.\n "
        f"если вы хотите добавить магазин, введите 3.\n"
        f"если вы хотите посмотреть список магазинов введите 4\n"
        f"если вы хотите посмотреть список покупателей введите 5\n"
        f"если вы хотите посмотреть список складов введите 6\n"
        f"если вы хотите узнать информацию о конкретном магазине нажмите 7\n"
        f"если вы хотите узнать информацию о конкретном покупателе нажмите 8\n"
        f"если вы хотите узнать информацию о конкретном складе нажмите 9\n"
        f"если вы хотите совершить покупку введите 10\n")
    while True:
        req=input()
        if req=="\help":
            print(
                f" если вы хотите увидеть список команд, введите \help\n "
                f"если вы хотите добавить покупателя, введите 1. \n"
                f" есля вы хотите добавить магазин, введите 2.\n "
                f"если вы хотите добавить магазин, введите 3.\n"
                f"если вы хотите посмотреть список магазинов введите 4\n"
                f"если вы хотите посмотреть список покупателей введите 5\n"
                f"если вы хотите посмотреть список складов введите 6\n"
                f"если вы хотите узнать информацию о конкретном магазине нажмите 7\n"
                f"если вы хотите узнать информацию о конкретном покупателе нажмите 8\n"
                f"если вы хотите узнать информацию о конкретном складе нажмите 9\n"
                f"если вы хотите совершить покупку введите 10\n")
        elif req=='1':
            name=input("введите имя покупателя: ")
            numofprod=int(input("введите количество изначального товара у покупателя: "))
            money=int(input("введите количество денег у покупателя: "))
            buyers[name]=Buyer(money,numofprod,name)
            print(f"покупатель {name} создан")
        elif req=='2':
            name=input("введите название магазина: ")
            money=int(input("введите изначальное количество денег у магазина: "))
            price=int(input("введите цену на товар в этом магазине: "))
            shops[name]=Shop(money,price,name)
            print(f"магазин {name} создан")
        elif req=='3':
            name=input("введите название склада: ")
            numofprod=int(input("введите введите количество товаров на складе: "))
            warehouses[name]=Warehouse(numofprod, name)
            print(f"магазин {name} создан")
        elif req == '4':
            if len(shops)>0:
                for i in shops:
                    print(i)
                print()
            else:
                print("магазинов еще создано не было")
        elif req == '6':
            if len(warehouses)>0:
                for i in warehouses:
                    print(i)
                print()
            else:
                print("складов еще создано не было")
        elif req == '5':
            if len(buyers)>0:
                for i in buyers:
                    print(i)
                print()
            else:
                print("покупателей еще создано не было")
        elif req == '7':
            name = input("введите название магазина о котором хотите узнать: ")
            shops[name].printShopParams()
        elif req == '8':
            name = input("введите имя покупателя о котором хотите узнать: ")
            buyers[name].printBuyerParams()
        elif req == '9':
            name = input("введите название склада о котором хотите узнать: ")
            warehouses[name].printWareParams()
        elif req == '10':
            buyername=input("введите имя покупателя: ")
            f=True
            if not buyers[buyername]:
                print("такого покупателя нет")
                f=False
            else:
                shopname = input("введите название магазина: ")
                if not shops[shopname]:
                    print("такого магазина нет")
                    f=False
                else:
                    warename = input("введите название склада: ")
                    if not warehouses[warename]:
                        print("такого склада нет")
                        f=False
            if f:
                kol = int(input("введите количество товара которое надо купить: "))
                buyers[buyername].sendToShop(kol, shops[shopname], warehouses[warename])






if __name__ == "__main__":
    main()