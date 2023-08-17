from abc import ABC, abstractmethod
from models.vacancy import Vacancy


class AbstractSaver(ABC):
    """
    Абстрактный класс определяющий методы для добавления и загрузки вакансий в файл JSON.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path

    @abstractmethod
    def save_vacancies(self, vacancies: list[Vacancy]) -> None:
        pass

    @abstractmethod
    def load_vacancies(self) -> list[Vacancy]:
        pass