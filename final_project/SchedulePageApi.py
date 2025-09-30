import allure
import requests
import json


class SchedulePageApi:
    """Класс тестирования API"""

    def __init__(self, url: str) -> None:
        self.url = url

    @allure.step("Получить токен")
    def get_token(self, token: str) -> dict:
        """"Метод получения токена"""
        my_headers = {}
        my_headers["token_global"] = token
        return my_headers

    @allure.step("Получить расписание только событий")
    def get_event(self, token: dict, body: dict) -> json:
        """"Метод получения событий"""

        resp = requests.post(self.url + "/v2/schedule/events", json=body, cookies=token)

        print("resp", resp)

        return resp

    @allure.step("Создать личное событие")
    def create_personal(self, token: dict, body: dict) -> json:
        """"Метод создания события"""
        print("я тут")
        resp = requests.post(self.url + "/v2/schedule/createPersonal", json=body, cookies=token)
        print("создал?", resp)

        return resp

    @allure.step("Удалить личное событие")
    def delete_personal(self, token: dict, body: dict) -> json:
        """"Метод удаления события"""

        resp = requests.post(self.url + "/v2/schedule/removePersonal", json=body, cookies=token)

        return resp

    @allure.step("Редактировать личное событие")
    def update_personal(self, token: dict, body: dict) -> json:
        """"Метод редактирования события"""

        resp = requests.post(self.url + "/v2/schedule/updatePersonal", json=body, cookies=token)

        return resp
