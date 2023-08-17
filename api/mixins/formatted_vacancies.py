from typing import List
from models.vacancy import Vacancy


class FormattedVacanciesMixin:
    """
    Миксин для добавления метода получения отформатированных вакансий.
    """

    def get_formatted_vacancies(self) -> List[Vacancy]:
        """
        Получение списка отформатированных вакансий.

        :return: Список объектов Vacancy.
        """
        formatted_vacancies = []
        for page in range(1, 20):
            vacancies_page = self._get_request(page=page)
            if len(vacancies_page) == 0:
                break
            for vacancy in vacancies_page:
                formatted_vacancy = self._format_vacancy(vacancy)
                if formatted_vacancy:
                    formatted_vacancies.append(formatted_vacancy)
        return formatted_vacancies