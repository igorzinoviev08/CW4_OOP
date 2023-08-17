from abc import ABC, abstractmethod
from typing import List, Dict
from models.vacancy import Vacancy


class BaseVacancyAPI(ABC):
    """
    Абстрактный базовый класс для работы с разными платформами вакансий.
    """

    def __init__(self, keyword: str):
        """
        Инициализация класса.

        :param keyword: Ключевое слово для поиска вакансий.
        """
        self.keyword = keyword

    @abstractmethod
    def _get_request(self, page: int) -> List[Dict]:
        """
        Абстрактный метод для выполнения запроса к API.

        :param page: Номер страницы запроса.
        :return: Список словарей JSON с данными о вакансиях.
        """
        pass

    @abstractmethod
    def _format_vacancy(self, vacancy_data: Dict) -> Vacancy:
        """
        Абстрактный метод для форматирования данных вакансии.

        :param vacancy_data: Словарь с данными о вакансии.
        :return: Объект Vacancy.
        """
        pass