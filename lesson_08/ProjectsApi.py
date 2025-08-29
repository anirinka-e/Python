import requests


class ProjectsApi:

    def __init__(self, url):
        self.url = url

    # Получить токен авторизации
    def get_token(self, creds):
        resp = requests.post(self.url + "/api-v2/auth/companies", json=creds)
        creds["companyId"] = resp.json()["content"][0]["id"]
        resp = requests.post(self.url + "/api-v2/auth/keys", json=creds)

        # print(resp)
        print(resp.json()["key"])
        assert resp.status_code == 201
        return resp.json()["key"]

    # Удавление токена
    def del_token(self, token):
        print(token)
        resp = requests.delete(self.url + "/api-v2/auth/keys/" + token)
        assert resp.status_code == 200

    # Авторизация
    def auth(self, creds):
        token = self.get_token(creds)
        my_headers = {}
        my_headers["Authorization"] = 'Bearer ' + token
        return my_headers

    # Создать проект
    def create_project(self, my_headers, title):
        body = {
            "title": title
        }

        resp = requests.post(self.url + "/api-v2/projects", json=body, headers=my_headers)

        print("create", resp)
        return resp.json()

    # Изменить проект
    def change_project(self, my_headers, id_project, title):
        body = {
            "title": title
        }

        resp = requests.put(self.url + "/api-v2/projects/" + id_project, json=body, headers=my_headers)
        print("change", resp)

        return resp.json()

    # Получить проект
    def get_project(self, my_headers, id_project):
        resp = requests.get(self.url + "/api-v2/projects/" + id_project, headers=my_headers)
        print("get", resp)

        return resp.json()
