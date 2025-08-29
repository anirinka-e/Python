import pytest
from ProjectsApi import ProjectsApi

api = ProjectsApi("https://ru.yougile.com")


@pytest.fixture
def my_headers():
    creds = {
        "login": "",
        "password": ""
    }
    my_headers = api.auth(creds)
    yield my_headers
    api.del_token(my_headers["Authorization"][7:])


def test_create_positive(my_headers):
    body = api.create_project(my_headers, "Шляпа")

    assert list(body.keys())[0] == "id"


def test_create_negative(my_headers):
    body = api.create_project(my_headers, 111)

    assert body["message"][0] == "title must be a string"


def test_change_positive(my_headers):
    body1 = api.create_project(my_headers, "Шляпа")
    body2 = api.change_project(my_headers, body1["id"], "Шапка")

    assert list(body2.keys())[0] == "id"
    assert body1["id"] == body2["id"]


def test_change_negative(my_headers):
    body1 = api.create_project(my_headers, "Шляпа")
    body2 = api.change_project(my_headers, body1["id"], 111)

    assert body2["message"][0] == "title must be a string"


def test_get_positive(my_headers):
    body1 = api.create_project(my_headers, "Шляпа")
    body2 = api.get_project(my_headers, body1["id"])

    assert list(body2.keys())[2] == "id"
    assert body1["id"] == body2["id"]
    assert body2["title"] == "Шляпа"


def test_get_negative(my_headers):
    body1 = api.create_project(my_headers, "Шляпа")
    body2 = api.get_project(my_headers, body1["id"] + "1")

    assert body2["message"] == "Проект не найден"
