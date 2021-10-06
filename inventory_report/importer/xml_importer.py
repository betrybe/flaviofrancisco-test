from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @staticmethod
    def validate_path(path):
        file_extension = path.split(".")[-1]
        if file_extension != "xml":
            raise ValueError("Arquivo inválido")

    @staticmethod
    def import_data(path):
        XmlImporter.validate_path(path)
        tree = ET.parse(path)
        root = tree.getroot()
        companies = []
        for items in root:
            company = {}
            for item in items:
                company[item.tag] = item.text
            companies.append(company)
        return companies
