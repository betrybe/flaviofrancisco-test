import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def read_csv_files(path):
        file = open(path)
        data = csv.DictReader(file, delimiter=",", quotechar='"')
        return [data for data in data]

    @staticmethod
    def read_json_files(path):
        file = open(path)
        result = json.load(file)
        return result

    @staticmethod
    def read_xml_files(path):
        tree = ET.parse(path)
        root = tree.getroot()
        companies = []
        for items in root:
            company = {}
            for item in items:
                company[item.tag] = item.text
            companies.append(company)
        return companies

    @staticmethod
    def import_data(path, report):
        file_extension = path.split(".")[-1]
        file = ""
        if file_extension == "csv":
            file = Inventory.read_csv_files(path)
        elif file_extension == "json":
            file = Inventory.read_json_files(path)
        elif file_extension == "xml":
            file = Inventory.read_xml_files(path)
        if report == "simples":
            return SimpleReport.generate(file)
        return CompleteReport.generate(file)
