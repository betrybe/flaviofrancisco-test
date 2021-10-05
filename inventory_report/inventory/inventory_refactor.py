from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor:
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, report):
        files = self.importer.import_data(path)
        for item in files:
            self.data.append(item)
        if report == "simples":
            return SimpleReport.generate(files, False)
        return CompleteReport.generate(files, True)

    def __iter__(self):
        return InventoryIterator(self.data)