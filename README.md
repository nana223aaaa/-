# Для лабы
🛒 Автоматизированное тестирование процесса покупки на saucedemo.com
Этот проект реализует end-to-end (E2E) тест, проверяющий полный цикл покупки на демо-сайте saucedemo.com.

Что проверяет тест:
✅ Авторизацию пользователя
✅ Добавление товара в корзину
✅ Оформление заказа
✅ Подтверждение успешного завершения покупки

⚙️ Системные требования
Python 3.7 или новее

Библиотеки: Selenium WebDriver

Браузер: Google Chrome (последняя версия)

ChromeDriver (версия должна соответствовать установленному Chrome)

🛠 Установка
Установите зависимости:

bash
pip install selenium
Скачайте ChromeDriver с официального сайта

Укажите путь к драйверу в коде (по умолчанию: D:/DriverChrome/chromedriver-win64/chromedriver.exe)

🚀 Запуск теста
Выполните команду в терминале:

bash
python -m pytest
(или через IDE: Run Module)

Тест автоматически проверит весь процесс покупки и выведет результат.
