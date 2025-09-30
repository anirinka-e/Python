import pytest
import allure
from SchedulePageApi import SchedulePageApi
from DataProvider import DataProvider

api = SchedulePageApi("https://api-teachers.skyeng.ru")


@pytest.fixture
def my_headers():
    token = DataProvider().get_token()
    my_headers = api.get_token(token)
    yield my_headers


@pytest.fixture
def body_events():
    body_events = DataProvider().get_body_events()
    yield body_events


@pytest.fixture
def body_date():
    body_date = DataProvider().get_body_date()
    yield body_date


@allure.title("Тестирование расписания")
@allure.description(
    "Тест проверяет вывод всех событий за период")
@allure.feature("Расписание")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_events(my_headers, body_events, body_date):
    """"Тест получения события"""

    with allure.step(f"Предусловие: создание события с телом {body_date["body"]}"):
        body = api.create_personal(my_headers, body_date["body"])
        id_event = body.json()['data']['payload']['id']

    with allure.step("Отправка запроса на получение всех событий за период"):
        body = api.get_event(my_headers, body_events)

    with allure.step(f"Постусловие: очистка от созданного запроса c id {id_event}"):
        body_date["body_del"]["id"] = id_event
        api.delete_personal(my_headers, body_date["body_del"])

    assert str(body) == "<Response [200]>"
    assert len(body.json()["data"]["events"]) >= 1


@allure.title("Тестирование расписания")
@allure.description(
    "Тест проверяет создание события")
@allure.feature("Личное событие")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_personal(my_headers, body_date):
    """"Тест создания события"""

    with allure.step(f"Отправка запроса на создание нового события с телом {body_date["body"]}"):
        body = api.create_personal(my_headers, body_date["body"])
        id_event = body.json()['data']['payload']['id']

    with allure.step(f"Постусловие: очистка от созданного запроса c id {id_event}"):
        body_date["body_del"]["id"] = id_event
        api.delete_personal(my_headers, body_date["body_del"])

    assert str(body) == "<Response [200]>"
    assert body.json()["data"]["type"] == "personal"
    assert body.json()["errors"] == None
    assert body.json()["data"]["payload"]["payload"]["title"] == "New event"


@allure.title("Тестирование расписания")
@allure.description(
    "Тест проверяет удаление события")
@allure.feature("Личное событие")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_personal(my_headers, body_date):
    """"Тест удаления события"""

    with allure.step(f"Предусловие: создание события с телом {body_date["body"]}"):
        body_create = api.create_personal(my_headers, body_date["body"])
        id_event = body_create.json()['data']['payload']['id']

    with allure.step(f"Отправка запроса на удаление запроса c id {id_event}"):
        body_date["body_del"]["id"] = id_event
        body = api.delete_personal(my_headers, body_date["body_del"])

    assert str(body) == "<Response [200]>"
    assert body.json()["data"] == True
    assert body.json()["errors"] == None


@allure.title("Тестирование расписания")
@allure.description(
    "Тест проверяет изменения названия события")
@allure.feature("Личное событие")
@allure.severity(allure.severity_level.CRITICAL)
def test_update_personal(my_headers, body_date):
    """"Тест создания события"""

    with allure.step(f"Предусловие: создание события с телом {body_date["body"]}"):
        body = api.create_personal(my_headers, body_date["body"])
        id_event = body.json()['data']['payload']['id']

    with allure.step("Отправка запроса на изменение названия"):
        body_date["body_update"]["id"] = id_event
        body_full = {**body_date["body"], **body_date["body_update"]}
        body_full["title"] = body_date["title_new"]

        body = api.update_personal(my_headers, body_full)
        id_event = body.json()['data']['payload']['id']

    with allure.step(f"Постусловие: очистка от созданного запроса c id {id_event}"):
        body_date["body_del"]["id"] = id_event
        api.delete_personal(my_headers, body_date["body_del"])

    assert str(body) == "<Response [200]>"
    assert body.json()["data"]["type"] == "personal"
    assert body.json()["errors"] == None
    assert body.json()["data"]["payload"]["payload"]["title"] == "New title"


@allure.title("Тестирование расписания")
@allure.description(
    "Тест проверяет изменения даты начала больше даты окончания события")
@allure.feature("Личное событие")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_personal_start_time_is_longer(my_headers, body_date):
    """"Тест создания события"""

    with allure.step("Изменение времени начала на большее"):
        body_date["body"]["startAt"] = body_date["oldStartAt_new"]

    with allure.step(f"Отправка запроса на создание нового события с телом {body_date["body"]}"):
        body = api.create_personal(my_headers, body_date["body"])

    assert body.json()["errors"][0]["error"]["message"] == "Date start must be earlier than end date"
