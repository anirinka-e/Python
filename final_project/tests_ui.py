import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from SchedulePageUI import SchedulePageUI
from DataProvider import DataProvider
from SchedulePageApi import SchedulePageApi

api = SchedulePageApi("https://api-teachers.skyeng.ru")


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(4)
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()


@pytest.fixture
def my_cookie():
    my_cookie = {
        'name': 'token_global',
        'value': DataProvider().get_token()
    }
    yield my_cookie


@pytest.fixture
def my_creds():
    my_creds = DataProvider().get_date("my_creds")
    yield my_creds


@allure.title("Тестирование Расписания")
@allure.description("Тест проверяет корректность создания события стандартного (серого) цвета")
@allure.feature("Личное событие")
@allure.severity(allure.severity_level.CRITICAL)
def test_sched(driver, my_creds):
    """Тест проверяет корректность работы добавления личного сообщения"""

    sched_page = SchedulePageUI(driver)

    with allure.step("Открытие страницы расписания"):
        sched_page.open_browser(my_creds)

    with allure.step("Перелистнуть страницу расписания"):
        sched_page.switch_table()

    with allure.step("Открытие окна добавления события"):
        sched_page.add_event(DataProvider().get_date("locator_events_ui"))

    with allure.step("Переключение на вкладку личного сообщения"):
        sched_page.switch_personal()

    with allure.step("Ввод названия события"):
        sched_page.input_personal_title("New event")

    with allure.step("Нажать кнопку сохранить"):
        sched_page.click_button_save()

    assert sched_page.chek_event_on_table() == True
    assert sched_page.clear_slot_event_api() == 1
    assert sched_page.chek_event_color_on_table("rgba(244, 245, 246, 1)") == True
    assert sched_page.chek_name_event() == "New event"


@allure.title("Тестирование Расписания")
@allure.description("Тест проверяет попытку создания с пустым названием")
@allure.feature("Поле названия")
@allure.severity(allure.severity_level.CRITICAL)
def test_empty_sched(driver, my_creds, my_cookie):
    """Тест проверяет корректность работы личного сообщения с пустым названием"""

    sched_page = SchedulePageUI(driver)

    with allure.step("Открытие страницы расписания"):
        sched_page.open_browser(my_creds)

    with allure.step("Перелистнуть страницу расписания"):
        sched_page.switch_table()

    with allure.step("Открытие окна добавления события"):
        sched_page.add_event(DataProvider().get_date("locator_events_ui"))

    with allure.step("Переключение на вкладку личного сообщения"):
        sched_page.switch_personal()

    assert sched_page.chek_button_active() == False
    assert sched_page.chek_name_valid() == False


@allure.title("Тестирование Расписания")
@allure.description("Тест проверяет попытку создания максимальным  количеством символов в названии (40 символов)")
@allure.feature("Поле названия")
@allure.severity(allure.severity_level.CRITICAL)
def test_40_symbol_sched(driver, my_creds, my_cookie):
    """Тест проверяет корректность работы создания максимальным  количеством символов в названии (40 символов)"""

    sched_page = SchedulePageUI(driver)

    with allure.step("Открытие страницы расписания"):
        sched_page.open_browser(my_creds)

    with allure.step("Перелистнуть страницу расписания"):
        sched_page.switch_table()

    with allure.step("Открытие окна добавления события"):
        sched_page.add_event(DataProvider().get_date("locator_events_ui"))

    with allure.step("Переключение на вкладку личного сообщения"):
        sched_page.switch_personal()

    with allure.step("Ввод названия события"):
        title = DataProvider().get_date_str("40_symbol")
        sched_page.input_personal_title(title)

    with allure.step("Нажать кнопку сохранить"):
        sched_page.click_button_save()

    assert sched_page.chek_event_on_table() == True
    assert sched_page.clear_slot_event_api() == 1
    assert sched_page.chek_event_color_on_table("rgba(244, 245, 246, 1)") == True
    assert sched_page.chek_name_event() == title


@allure.title("Тестирование Расписания")
@allure.description(
    "Тест проверяет попытку создания с количеством символов больше максимального в названии (41 символов)")
@allure.feature("Поле названия")
@allure.severity(allure.severity_level.CRITICAL)
def test_41_symbol_sched(driver, my_creds, my_cookie):
    """Тест проверяет корректность работы создания с количеством символов больше максимального в названии (41 символов)"""

    sched_page = SchedulePageUI(driver)

    with allure.step("Открытие страницы расписания"):
        sched_page.open_browser(my_creds)

    with allure.step("Перелистнуть страницу расписания"):
        sched_page.switch_table()

    with allure.step("Открытие окна добавления события"):
        sched_page.add_event(DataProvider().get_date("locator_events_ui"))

    with allure.step("Переключение на вкладку личного сообщения"):
        sched_page.switch_personal()

    with allure.step("Ввод названия события в 41 символ"):
        title = DataProvider().get_date_str("40_symbol")
        sched_page.input_personal_title(title + ".")

    with allure.step("Нажать кнопку сохранить"):
        sched_page.click_button_save()

    assert sched_page.chek_event_on_table() == True
    assert sched_page.clear_slot_event_api() == 1
    assert sched_page.chek_event_color_on_table("rgba(244, 245, 246, 1)") == True
    assert len(sched_page.chek_name_event()) == 40


@allure.title("Тестирование Расписания")
@allure.description("Тест проверяет попытку создания события с другим цветом (желтым)")
@allure.feature("Цвет")
@allure.severity(allure.severity_level.CRITICAL)
def test_color_sched(driver, my_creds, my_cookie):
    """Тест проверяет корректность работы создания события с другим цветом (желтым)"""

    sched_page = SchedulePageUI(driver)

    with allure.step("Открытие страницы расписания"):
        sched_page.open_browser(my_creds)

    with allure.step("Перелистнуть страницу расписания"):
        sched_page.switch_table()

    with allure.step("Открытие окна добавления события"):
        sched_page.add_event(DataProvider().get_date("locator_events_ui"))

    with allure.step("Переключение на вкладку личного сообщения"):
        sched_page.switch_personal()

    with allure.step("Ввод названия события"):
        sched_page.input_personal_title("New event")

    with allure.step("Переключение цвета"):
        sched_page.switch_color(".cursor-pointer.flex-none.color-circle.mr10.ng-star-inserted")

    with allure.step("Нажать кнопку сохранить"):
        sched_page.click_button_save()

    assert sched_page.chek_event_on_table() == True
    assert sched_page.chek_event_color_on_table("rgba(255, 247, 199, 1)") == True
    assert sched_page.chek_name_event() == "New event"
    assert sched_page.clear_slot_event_api() == 1
