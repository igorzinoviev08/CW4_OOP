import requests

from api.mixins.formatted_vacancies import FormattedVacanciesMixin
from models.vacancy import Vacancy
from utils.currency_converter import get_currency_data
from api.parser import BaseVacancyAPI
from typing import List, Dict


class HHVacancyAPI(BaseVacancyAPI, FormattedVacanciesMixin):
    """
    Класс для работы с платформой hh.ru.
    """
    url = "https://api.hh.ru/vacancies"

    def __init__(self, keyword: str):
        """
        Инициализация класса.

        :param keyword: Ключевое слово для поиска вакансий.
        """
        super().__init__(keyword)

    def _get_request(self, page: int) -> List[Dict]:
        """
        Получение данных о вакансиях через API hh.ru.

        :param page: Номер страницы запроса.
        :return: Список словарей JSON с данными о вакансиях.
        """
        params = {
            'only_with_salary': True,
            "per_page": 100,
            "page": page,
            "text": self.keyword,
            "archived": True
        }
        try:
            response = requests.get(self.url, params=params)
            response.raise_for_status()
            return response.json().get("items", [])
        except requests.exceptions.RequestException as e:
            print("An error occurred while making the request:", e)
            return []

    def _format_vacancy(self, vacancy_data: Dict) -> Vacancy:
        """
        Форматирование данных о вакансии для платформы hh.ru.

        :param vacancy_data: Словарь с данными о вакансии.
        :return: Объект Vacancy.
        """
        if self.keyword.lower() in vacancy_data["name"].lower():
            url = vacancy_data["alternate_url"]
            title = vacancy_data["name"]
            employer = vacancy_data["employer"]["name"]
            salary_from = vacancy_data["salary"]["from"] if vacancy_data["salary"]["from"] is not None else 0

            if vacancy_data["salary"]["currency"].upper() not in ["RUR", "RUB"] and vacancy_data["salary"]["from"]:
                salary_from *= get_currency_data(vacancy_data["salary"]["currency"])

            return Vacancy(title, url, salary_from, employer)