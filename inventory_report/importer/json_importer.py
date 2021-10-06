from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def validate_path(path):
        file_extension = path.split(".")[-1]
        if file_extension != "json":
            raise ValueError("Arquivo inválido")

    @staticmethod
    def import_data(path):
        JsonImporter.validate_path(path)
        file = open(path)
        result = json.load(file)
        return result
