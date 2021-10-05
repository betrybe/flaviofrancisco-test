from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
import sys


def main():
    
    if len(sys.argv) < 3:
        return print("Verifique os argumentos", file=sys.stderr)
    
    for arg in sys.argv:
        if arg == "":
            return print("Verifique os argumentos", file=sys.stderr)
        
    file_name, path, report_type = sys.argv
    file_type = path.split(".")[1]

    importer_type_dict = {
        "csv": CsvImporter,
        "json": JsonImporter,
        "xml": XmlImporter,
    }

    importer = importer_type_dict[file_type]
    my_report = InventoryRefactor(importer)
    result = my_report.import_data(path, report_type)
    print(result)
    return '' + result

if __name__ == "__main__":
    main()
