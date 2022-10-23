from parsejs import FileManager


class Buyer(object):
    def __init__(self, money=0, numberofproduct=0, id="p"):
        self.id = id
        self.file = FileManager(id)
        self.file.write_xml({'numberofproduct': numberofproduct, 'money': money})

    def getname(self):
        return self.id

    def setBuyerParams(self, money=0, numberofproduct=0, id="p"):
        self.id = id
        self.file = FileManager(id)
        self.file.write_xml({'numberofproduct': numberofproduct, 'money': money})

    def printBuyerParams(self):
        print(
            f'денег у покупателя:{self.file.read_xml()["data"]["money"]}. продуктов у покупателя:\
{self.file.read_xml()["data"]["numberofproduct"]}')

    def getBuyerParams(self):
        return self.file.read_xml()["data"]["money"], self.file.read_xml()["data"]["numberofproduct"]

    def sendToShop(self, kol, shop, ware):
        try:
            a,b=shop.actfromBuyer(kol, int(self.file.read_xml()["data"]["money"]), ware)
            if a:
                shop.acttoware(kol, ware)
                self.file.write_xml({'numberofproduct': int(self.file.read_xml()["data"]["numberofproduct"]) + kol,
                                 'money': int(self.file.read_xml()["data"]["money"]) - b})
        except: pass
