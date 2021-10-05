#importando os métodos abstratos da classe em Importer
from inventory_report.importer.importer import Importer
import csv

#criando classe para importar caminho com 
class CsvImporter(Importer):
    @staticmethod
    def validate_path(path):
        file_extension = path.split(".")[-1]
        if file_extension != "csv":
            raise ValueError("Arquivo inválido")

    @staticmethod
    def import_data(path):
        CsvImporter.validate_path(path)
        file = open(path)
        data = csv.DictReader(file, delimiter=",", quotechar='"')
        return [data for data in data]
