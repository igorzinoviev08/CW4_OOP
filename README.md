# CW4_OOP

1. Программа работает с API сайтов  Head Hunter и Super Job
2. Программа позволяет отстортировать и вывести список топ вакансий раздельно с каждого сайта и с общего ресурса.
3. Топ вакансий выводится в файл в json формате.
4. Программа запускается файлом main.py.
5. Для работы с API используется метод request.
6. В программе реализован абстрактный метод для возможности работы с разными классами и файлами.


Класс, наследующийся от абстрактного класса, для работы с платформой hh.ru

class HHVacancyAPI(ParserAPI):



Метод для подключения к API

def get_request(self):



Метод для форматирования списка словарей с вакансиями

def get_formatted_vacancies(self):



class SuperJobVacancyAPI(ParserAPI):
    """
    Класс, наследующийся от абстрактного класса,
    для работы с платформой superjob

class JsonSaver:
    
    Класс определяющий методы для добавления вакансий в файл


    def add_vacancy(self, vacancy):
        """
        Метод для добавления вакансии в файл



class Vacancy:
    
    Класс для представления вакансии



class JobParser:
    """
    Класс для представления приложения





    def hh_search_vacancy(self):
        
        Метод для поиска вакансий на hh.ru


    def sj_search_vacancy(self):
        
        Метод для поиска вакансий на superjob

    
def all_search_vacancy(self):
        
        Метод для поиска вакансий c двух платформ


    def sorted_vacancies(self):
        """
        Метод для сортировки вакансий по зп


    def write_file(self):
        """
        Метод для записи полученных вакансий в файл


    def user_interaction(self):
        """
        Интерактив для пользователя


    def sub_user_interaction(self):
        """
        Подинтерактив для пользователя
