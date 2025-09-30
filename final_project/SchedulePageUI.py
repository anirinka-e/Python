import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from SchedulePageApi import SchedulePageApi
from DataProvider import DataProvider


class SchedulePageUI:
    """Класс тестирования UI"""

    def __init__(self, driver) -> None:
        self.driver = driver
        self.waiter = WebDriverWait(driver, 10)
        self.url = "https://teachers.skyeng.ru/schedule/"
        self.api = "https://api-teachers.skyeng.ru"

    # @allure.step("Открытие страницы")
    # def open_browser(self):
    #     """Открывает браузер на заданной в коде странице и разворачивает окно на весь экран"""
    #
    #     self.driver.implicitly_wait(10)
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()

    @allure.step("Ввод логина и пароля: login и password")
    def input_login(self, my_creds: dict):
        """Вводит в поля значения login и password"""

        self.driver.find_element(
            By.CSS_SELECTOR, "[name=username]"
        ).send_keys(my_creds["login"])
        self.driver.find_element(By.CSS_SELECTOR, "[name=password]").send_keys(my_creds["password"])

    @allure.step("Нажатие на кнопку Login")
    def click_login(self):
        """Нажимает на кнопку Login"""

        self.driver.find_element(
            By.CSS_SELECTOR, "button"
        ).click()

    @allure.step("Очистка слотов событий в календаре")
    def clear_slot_event_api(self) -> int:
        my_headers = SchedulePageApi(self.api).get_token(DataProvider().get_token())
        body = DataProvider().get_body_events()
        body_del = DataProvider().get_body_date()

        resp = SchedulePageApi(self.api).get_event(my_headers, body)
        resp_events = resp.json()["data"]["events"]

        count_events = len(resp_events)

        if len(resp_events) != 0:
            print("Есть события")
            for item in range(len(resp_events)):
                body_del["body_del"]["id"] = resp_events[item]["payload"]["id"]
                body_del["body_del"]["startAt"] = resp_events[item]["startAt"]
                SchedulePageApi(self.api).delete_personal(my_headers, body_del["body_del"])

        return count_events

    @allure.step("Открытие страницы Расписания")
    def open_browser(self, my_creds: dict) -> None:
        """Открывает браузер на заданной в коде странице и разворачивает окно на весь экран"""

        self.driver.get(self.url)
        self.driver.maximize_window()
        self.input_login(my_creds)
        self.click_login()
        self.clear_slot_event_api()

        self.waiter.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".page-layout")
            )
        )

    @allure.step("Переключение страницы Расписания на следующую")
    def switch_table(self) -> None:
        """Перелистывает страницу на следующую неделю"""

        date = self.driver.find_element(
            By.CSS_SELECTOR, "div[_ngcontent-c15].text-container"
        ).text

        self.driver.find_element(By.CSS_SELECTOR, ".svg-inline--fa.fa-chevron-right.fa-w-10.fa-fw").click()
        self.waiter.until_not(
            EC.text_to_be_present_in_element_value(
                (By.CSS_SELECTOR, "div[_ngcontent-c15].text-container"), date
            )
        )

    @allure.step("Открытие окна добавления события")
    def add_event(self, event) -> None:
        self.driver.find_element(By.CSS_SELECTOR, event).click()

    @allure.step("Переключение на вкладку личного сообщения")
    def switch_personal(self) -> None:
        self.driver.find_element(By.XPATH, "//span[text()=' Личное событие ']").click()

    @allure.step("Переключение цвета личного сообщения")
    def switch_color(self, color) -> None:
        print(color)
        self.driver.find_element(By.CSS_SELECTOR, color).click()

    @allure.step("Ввод названия события")
    def input_personal_title(self, title) -> None:
        self.waiter.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "input.width-100")
            )
        )
        self.driver.find_element(By.CSS_SELECTOR, "input.width-100").send_keys(title)

    @allure.step("Нажатие кнопки Сохранить")
    def click_button_save(self) -> None:
        self.waiter.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "button.root.-type-primary.-color-brand.-size-m.-active")
            )
        )
        self.driver.find_element(By.CSS_SELECTOR, "button.root.-type-primary").click()

    @allure.step("Проверка отображения события на доске")
    def chek_event_on_table(self) -> bool:
        try:
            self.driver.find_element(By.CSS_SELECTOR, ".personal-container.event-block__container")
            exist = True
        except ArithmeticError:
            exist = False
        print("exist", exist)
        return exist

    @allure.step("Проверка названия события")
    def chek_name_event(self) -> bool:
        result = self.driver.find_element(
            By.CSS_SELECTOR, ".long-view__title"
        ).text

        return result

    @allure.step("Проверка отображения активности кнопки Сохранить при невалидных данных")
    def chek_button_active(self) -> bool:
        print("проверяю кнопку")
        self.waiter.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "button.root.-type-primary.-color-brand.-size-m")
            )
        )
        active = True
        try:
            self.driver.find_element(By.CSS_SELECTOR, "button.root.-type-primary.-color-brand.-size-m.-active")
            print("активно")
        except:
            print("не активно")
            active = False

        return active

    @allure.step("Проверка валидности названия события")
    def chek_name_valid(self) -> bool:
        self.waiter.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "input.width-100")
            )
        )
        valid = False

        try:
            self.driver.find_element(By.CSS_SELECTOR,
                                     "input.width-100.mt8.-size-m.-skin-normal.ng-untouched.ng-pristine.ng-invalid")
            print("не валидно")
        except:
            print("валидно")
            valid = True

        return valid

    @allure.step("Проверка проверка цвета")
    def chek_event_color_on_table(self, color: str) -> bool:
        self.driver.find_element(By.CSS_SELECTOR, ".personal-container.event-block__container")
        if self.waiter.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".personal-container.event-block__container"))).value_of_css_property(
            "background-color") == color:
            exist = True
        else:
            exist = False

        return exist
