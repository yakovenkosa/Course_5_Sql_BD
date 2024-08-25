import psycopg2

from config import config


class DBManager:
    """
    Класс DBManager для подключения к БД PostgreSQL.
    """

    def __init__(self):
        db_params = config()
        self.conn = psycopg2.connect(**db_params)

    def get_companies_and_vacancies_count(self):
        """
        Функция для получения списка компаний и количество вакансий в каждой.
        """
        cur = self.conn.cursor()
        cur.execute(
            """SELECT c.company_name, COUNT(v.company_id) as vacancies_count\n
                       FROM companies c
                       LEFT JOIN vacancies v ON c.id = v.company_id
                       GROUP BY c.company_name;"""
        )
        self.conn.commit()
        return cur.fetchall()

    def get_all_vacancies(self):
        """
        Функция для получения списка вакансий с указанием названия компании,
        зарплаты и ссылки на вакансию.
        """
        cur = self.conn.cursor()
        cur.execute()
        return cur.fetchall()

    def get_avg_salary(self):
        """
        Функция для получения среднюй зарплаты по вакансиям.
        """
        cur = self.conn.cursor()
        cur.execute(
            """SELECT AVG(salary_from + salary_to) / 2
                       FROM vacancies"""
        )
        return cur.fetchone()[0]

    def get_vacancies_with_higher_salary(self):
        """
        Функция для получения списка вакансий, у которых зарплата
        выше средней по вакансиям.
        """
        cur = self.conn.cursor()
        cur.execute()
        return cur.fetchall()

    def get_vacancies_with_keyword(self, keyword):
        """
        Функция для получения списка вакансий, в содержащих название
        переданное в метод слова.
        """
        cur = self.conn.cursor()
        cur.execute()
        return cur.fetchall()
