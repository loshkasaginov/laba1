import json
from dict2xml import dict2xml
import xmltodict

class FileManager():
    def __init__(self,id) :
        self.id=id

    def write_json(self, ar):
        with open(f'json{self.id}.json', 'w') as outfile:
            json.dump(ar, outfile)

    def read_json(self):
        with open(f'json{self.id}.json', "r") as json_file:
            data = json.load(json_file)
        return data

    def write_xml(self, *args):
        for ar in args:
            with open(f'xml{self.id}.xml', "w") as outfile:
                outfile.write(dict2xml(ar, wrap='data'))

    def read_xml(self):
        xml_file = open(f'xml{self.id}.xml', 'r')
        xml_content = xml_file.read()
        return xmltodict.parse(xml_content)