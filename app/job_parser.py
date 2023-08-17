from json import JSONDecodeError

from api.super_job_vacancy_api import SuperJobVacancyAPI
from api.hh_vacancy_api import HHVacancyAPI
from app.job_parser_meta import JobSearchAppMeta
from file_saver.json_saver import JsonSaver


class JobParser(metaclass=JobSearchAppMeta):
    """
    Класс для представления приложения
    """

    json_saver = JsonSaver("vacancies.json")
    all_vacancies = []
    job_title = ''

    @classmethod
    def __hh_search_vacancy(cls) -> None:
        """
        Метод для поиска вакансий на hh.ru
        """
        hh_vac = HHVacancyAPI(cls.job_title)
        cls.all_vacancies = hh_vac.get_formatted_vacancies()

    @classmethod
    def __sj_search_vacancy(cls) -> None:
        """
        Метод для поиска вакансий на superjob
        """
        sj_vac = SuperJobVacancyAPI(cls.job_title)
        cls.all_vacancies = sj_vac.get_formatted_vacancies()

    @classmethod
    def __all_search_vacancy(cls) -> None:
        """
        Метод для поиска вакансий c двух платформ
        """
        sj_vac = SuperJobVacancyAPI(cls.job_title)
        hh_vac = HHVacancyAPI(cls.job_title)
        cls.all_vacancies = hh_vac.get_formatted_vacancies() + sj_vac.get_formatted_vacancies()

    @classmethod
    def __sorted_vacancies(cls) -> None:
        """
        Метод для сортировки вакансий по зп
        """
        top_vacancy = int(input("Введите топ вакансий по зп: "))
        cls.all_vacancies = sorted(cls.all_vacancies, reverse=True)[:top_vacancy]

    @classmethod
    def __read_file(cls) -> None:
        """
            Метод для загрузки вакансий из файла
        """
        print("Хотите загрузить вакансии из файла? \n"
              "Да 1\n"
              "Нет 2\n")
        while True:
            user_input = int(input())
            if user_input == 1:
                try:
                    cls.json_saver.load_vacancies()
                except (FileNotFoundError,JSONDecodeError) as e:
                    print(e)
                break
            elif user_input == 2:
                break
            else:
                print("Введено неверное значение")
        print("Нужно ли искать новые вакансии?\n"
              "Да 1\n"
              "Нет 2\n")
        while True:
            user_input = int(input())
            if user_input == 1:
                break
            elif user_input == 2:
                exit()
            else:
                print("Введено неверное значение")

    @classmethod
    def __write_file(cls) -> None:
        """
        Метод для записи полученных вакансий в файл
        """
        print("Хотите записать вакансии в файл? \n"
              "Да 1\n"
              "Нет 2\n")
        while True:
            user_input = int(input())
            if user_input == 1:
                cls.json_saver.save_vacancies(
                    [vacancy.to_json() for vacancy in cls.all_vacancies])  # Запись JSON-представления вакансий
                break
            elif user_input == 2:
                break
            else:
                print("Введено неверное значение")

    @classmethod
    def _user_interaction(cls) -> None:
        """
        Интерактив для пользователя
        """
        cls.__read_file()
        cls.job_title = str(input("Введите название профессии: "))
        print("\nДля поиска с hh.ru Нажмите 1\n"
              "Для поиска с SuperJob 2\n"
              "Для поиска с hh.ru и SuperJob 3\n"
              "Для выхода 0")
        while True:
            user_input = int(input())
            if user_input == 1:
                cls.__hh_search_vacancy()
                cls.__sub_user_interaction()
                break
            elif user_input == 2:
                cls.__sj_search_vacancy()
                cls.__sub_user_interaction()
                break
            elif user_input == 3:
                cls.__all_search_vacancy()
                cls.__sub_user_interaction()
                break
            elif user_input == 0:
                exit()
            else:
                print("Введено неверное значение")
        cls.__write_file()

    @classmethod
    def __sub_user_interaction(cls) -> None:
        """
        Подинтерактив для пользователя
        """
        while True:
            user_input = int(input("Хотите ли отсортировать вакансии?\n"
                                   "Да 1\n"
                                   "Нет 2\n"))
            if user_input == 1:
                cls.__sorted_vacancies()
                break
            elif user_input == 2:
                break
            else:
                print("Введено неверное значение")

        [print(vacancy) for vacancy in cls.all_vacancies]