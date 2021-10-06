from datetime import date, datetime


class SimpleReport:

    @staticmethod
    def get_company_with_most_products(companies_list):
        most_shown, quantity = "", 0
        for comparator in companies_list:
            current_quantity = 0
            for compared in companies_list:
                if (
                    comparator["nome_da_empresa"]
                    == compared["nome_da_empresa"]
                ):
                    current_quantity += 1
            if current_quantity > quantity:
                most_shown = comparator["nome_da_empresa"]
                quantity = current_quantity
        return most_shown

    @staticmethod
    def get_oldest_production_of_a_company(companies_list, company):
        dates = []
        for item in companies_list:
            if item["nome_da_empresa"] == company:
                dates.append(
                    datetime.strptime(
                        item["data_de_fabricacao"], "%Y-%m-%d"
                    ).date()
                )
        dates.sort()
        return dates[0]

    @staticmethod
    def get_nearest_expiration_date(companies_list, company):
        dates = []
        now = date.today()
        for item in companies_list:
            expiration = datetime.strptime(
                item["data_de_validade"], "%Y-%m-%d"
            ).date()
            if item["nome_da_empresa"] == company and expiration >= now:
                dates.append(expiration)
        dates.sort()
        return dates[0]

    @staticmethod
    def generate(companies_list, barra_n=True):
        company_name = SimpleReport.get_company_with_most_products(
            companies_list
        )
        production_date = SimpleReport.get_oldest_production_of_a_company(
            companies_list, company_name
        )
        expiration_date = SimpleReport.get_nearest_expiration_date(
            companies_list, company_name
        )
        result = (
            f"Data de fabricação mais antiga: {production_date}\n"
            f"Data de validade mais próxima: {expiration_date}\n"
            "Empresa com maior quantidade de produtos "
            f"estocados: {company_name}"
        )
        if barra_n:
            result += '\n'
        return result
