from parsejs import FileManager


class Warehouse(object):
    def __init__(self, numberofproduct=0, id='l'):
        self.id = id
        self.file = FileManager(id)
        self.file.write_json({'numberofproduct': numberofproduct})

    def setWareParams(self, numberofproduct=0):
        self.file.write_json({'numberofproduct': numberofproduct})

    def getname(self):
        return self.id

    def printWareParams(self):
        print(f'продуктов на складе:{int(list(self.file.read_json().values())[0])}')

    def getWareParams(self):
        return int(list(self.file.read_json().values())[0])

    def acc(self, kol):
        a=int(list(self.file.read_json().values())[0])
        a-=kol
        self.file.write_json({'numberofproduct': a})
