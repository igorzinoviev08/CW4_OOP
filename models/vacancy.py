class Vacancy:
    """
    Класс для представления вакансии.
    """
    __slots__ = ('title', 'url', 'salary_from', 'employer')

    def __init__(self, title: str, url: str, salary_from: int, employer: str):
        """
        Инициализация объекта вакансии.

        :param title: Название вакансии.
        :param url: URL вакансии.
        :param salary_from: Зарплата "от".
        :param employer: Работодатель.
        """
        self.title = title
        self.url = url
        self.salary_from = int(salary_from)
        self.employer = employer

    def __str__(self) -> str:
        """
        Возвращает строковое представление вакансии.

        :return: Строковое представление вакансии.
        """
        return f"{self.title} {self.salary_from} ({self.url})"

    def __gt__(self, other) -> bool:
        """
        Оператор "больше" для сравнения вакансий по зарплате "от".

        :param other: Другая вакансия для сравнения.
        :return: True, если текущая вакансия имеет большую зарплату "от" другой вакансии.
        """
        return self.salary_from > other.salary_from

    def to_json(self) -> dict[str]:
        """
        Возвращает JSON-представление объекта вакансии.

        :return: JSON-представление объекта вакансии.
        """
        vacancy_dict = {
            "title": self.title,
            "url": self.url,
            "salary_from": str(self.salary_from),  # Преобразование в строку
            "employer": self.employer
        }
        return vacancy_dict

    @classmethod
    def from_json(cls, json_str: str) -> 'Vacancy':
        """
        Создает объект вакансии из JSON-представления.

        :param json_str: JSON-представление объекта вакансии.
        :return: Объект вакансии.
        """
        return cls(**json_str)