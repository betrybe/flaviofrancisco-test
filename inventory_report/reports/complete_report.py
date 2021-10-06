from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def stocked_products_by_company(companies_list):
        companies = {}
        for item in companies_list:
            if item["nome_da_empresa"] in companies:
                companies[item["nome_da_empresa"]] += 1
            if item["nome_da_empresa"] not in companies:
                companies[item["nome_da_empresa"]] = 1
        return companies

    @staticmethod
    def generate(companies_list, barra_n=False):
        company_name = SimpleReport.get_company_with_most_products(
            companies_list
        )
        production_date = SimpleReport.get_oldest_production_of_a_company(
            companies_list, company_name
        )
        expiration_date = SimpleReport.get_nearest_expiration_date(
            companies_list, company_name
        )
        companies = CompleteReport.stocked_products_by_company(companies_list)
        answer = (
            f"Data de fabricação mais antiga: {production_date}\n"
            f"Data de validade mais próxima: {expiration_date}\n"
            "Empresa com maior quantidade de produtos "
            f"estocados: {company_name}\n\n"
            "Produtos estocados por empresa: \n"
        )
        minha_lista = list(companies.keys())
        for company in minha_lista:
            if (
                len(minha_lista) - 1 == minha_lista.index(company)
                and barra_n
            ):
                answer += f"- {company}: {companies[company]}"
            else:
                answer += f"- {company}: {companies[company]}\n"
        return answer
