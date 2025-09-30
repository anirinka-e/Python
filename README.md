# Python

## Шаблон для автоматизации тестирования

### Шаги
1. Склонировать проект 'git clone https://github.com/anirinka-e/Python.git'
2. Установить зависимости pip3 install > -r requirements.txt
3. Настроить данные входа (логин, пароль, токен) в файле test_data.json
4. Запустить тесты 'pytest'
   - Для запуска всех тестов прописать в терминале pytest final_project
   - Для запуска только API тестов прописать в терминале pytest final_project/tests_api.py
   - Для запуска только UI тестов прописать в терминале pytest final_project/tests_ui.py
5. Сгенерировать отчет 'allure generate allure-files -o allure-report'
6. Открыть отчет 'allure open allure-report'

### Стек:
- pytest
- selenium
- requests
- allure
- config
- json

### Структура
- ./test - тесты
- ./pages - описание страниц
- ./api - хелперы для работы с API
- ./testdata — провайдер тестовых данных
    - test_data.json

### Полезные ссылки
- [Подсказка по markdown] (https://www.markdownguide.org/basic-syntax/)
- [Подсказка по .gitignore] (https://www.toptal.com/developers/gitignore)

### Библиотеки
- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install allure-pytest
- pip install requests