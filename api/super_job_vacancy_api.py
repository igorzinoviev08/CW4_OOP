
import os

import requests


from api.parser import ParserAPI
from models.vacancy import Vacancy
from utils.currency_converter import get_currency_data


class SuperJobVacancyAPI(ParserAPI):
    """
    Класс, наследующийся от абстрактного класса,
    для работы с платформой superjob
    """
    url = "https://api.superjob.ru/2.0/vacancies/"

    def __init__(self, keyword):
        self.keyword = keyword
        self.params = {
            "count": 100,
            "page": 1,
            "keywords": [[1, keyword]],
            "archived": False
        }
        self.headers = {
            "X-Api-App-Id": 'v3.r.126346210.19bcc737f1e3c2cc25555883f327544a579296fa.9cf8e122bc29d60287e5d00116238334efa8d24c'
        }
        self.vacancies = self.get_request()

    def get_request(self):
        """
        Метод для подключения к апи
        :return: список словарей json
        """
        response = requests.get(self.url, headers=self.headers, params=self.params)

        return response.json()["objects"]

    def get_formatted_vacancies(self):
        """
        Метод для форматирования списка словарей с вакансиями
        :return: приведенный к нужному виду список словарей
        """
        formatted_vacancies = []

        for vacancy in self.vacancies:
            if self.keyword.lower() in vacancy["profession"].lower():
                url = vacancy["link"]
                title = vacancy["profession"]
                employer = vacancy['firm_name']
                salary_from = vacancy['payment_from']
                if vacancy["currency"].upper() not in ["RUR", "RUB"] and vacancy['payment_from']:
                    salary_from *= get_currency_data(vacancy["currency"])
                formatted_vacancies.append(Vacancy(title, url, salary_from, employer))
            return formatted_vacancies