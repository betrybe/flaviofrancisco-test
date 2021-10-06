from abc import ABC, abstractclassmethod


class Importer(ABC):

    @abstractclassmethod
    def import_data():
        pass

    @abstractclassmethod
    def validate_path():
        pass
