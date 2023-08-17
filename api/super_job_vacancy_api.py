import os
import requests

from api.mixins.formatted_vacancies import FormattedVacanciesMixin
from models.vacancy import Vacancy
from utils.currency_converter import get_currency_data
from api.parser import BaseVacancyAPI
from typing import List, Dict


class SuperJobVacancyAPI(BaseVacancyAPI, FormattedVacanciesMixin):
    """
    Класс для работы с платформой SuperJob.
    """

    url = "https://api.superjob.ru/2.0/vacancies/"

    def __init__(self, keyword: str):
        """
        Инициализация класса.

        :param keyword: Ключевое слово для поиска вакансий.
        """
        super().__init__(keyword)
        self.headers = {
            "X-Api-App-Id": os.getenv('API_SUPERJOB_KEY')
        }

    def _get_request(self, page: int) -> List[Dict]:
        """
        Получение данных о вакансиях через API SuperJob.

        :param page: Номер страницы запроса.
        :return: Список словарей JSON с данными о вакансиях.
        """
        params = {
            "count": 100,
            "page": page,
            "keywords": [[1, self.keyword]],
            'archived': False
        }
        try:
            response = requests.get(self.url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json().get("objects", [])
        except requests.exceptions.RequestException as e:
            print("An error occurred while making the request:", e)
            return []

    def _format_vacancy(self, vacancy_data: Dict) -> Vacancy:
        """
        Форматирование данных о вакансии для платформы SuperJob.

        :param vacancy_data: Словарь с данными о вакансии.
        :return: Объект Vacancy.
        """
        if self.keyword.lower() in vacancy_data["profession"].lower():
            url = vacancy_data["link"]
            title = vacancy_data["profession"]
            employer = vacancy_data["firm_name"]
            salary_from = vacancy_data["payment_from"]

            if vacancy_data["currency"].upper() not in ["RUR", "RUB"] and vacancy_data["payment_from"]:
                salary_from *= get_currency_data(vacancy_data["currency"])

            return Vacancy(title, url, salary_from, employer)