import json

from file_saver.abc_saver import AbstractSaver
from models.vacancy import Vacancy


class JsonSaver(AbstractSaver):
    """
    Класс определяющий методы для добавления вакансий в файл JSON.
    """

    def __init__(self, file_path: str):
        super().__init__(file_path)

    def save_vacancies(self, vacancies: list[Vacancy]) -> None:
        """
        Метод для добавления вакансий в файл.

        :param vacancies: Список объектов вакансий для добавления.
        """
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, indent=4, ensure_ascii=False)

    def load_vacancies(self) -> None:
        """
        Метод для загрузки вакансий из файла.

        :return: Список объектов вакансий.
        """
        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            [print(Vacancy.from_json(json_str)) for json_str in data]