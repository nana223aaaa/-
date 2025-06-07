from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

def test_purchase_flow():
    driver_path = "D:/DriverChrome/chromedriver-win64/chromedriver.exe"
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)
    
    try:
        print("\n ТЕСТ НАЧИНАЕТСЯ \n")
        
        # 1. Авторизация
        print("Шаг 1: Авторизация")
        driver.get("https://www.saucedemo.com/")
        time.sleep(5)
        driver.save_screenshot("1_login_page.png")
        
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(10)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(5)
        
        # 2. Добавление товара
        print("\nШаг 2: Добавление товара")
        add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        add_button.click()
        print("Кнопка 'Add to cart' нажата")
        time.sleep(10)
        
        # 3. Проверка корзины
        print("\nШаг 3: Проверка корзины")
        try:
            cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
            print(f"Найдено товаров в корзине: {cart_badge.text}")
        except:
            print("Элемент shopping_cart_badge не найден!")
            print("Пробую найти корзину другими способами...")
            
            # Альтернативный поиск корзины
            cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
            print("Иконка корзины найдена, перехожу в корзину")
            cart_icon.click()
            time.sleep(10)
            
            # Проверка содержимого корзины
            try:
                item = driver.find_element(By.CLASS_NAME, "inventory_item_name")
                print(f"В корзине найден товар: {item.text}")
            except:
                print("Корзина пуста!")
                raise Exception("Товар не добавился в корзину")
        
        # 4. Оформление заказа
        print("\nШаг 4: Оформление заказа")
        driver.get("https://www.saucedemo.com/cart.html")
        time.sleep(10)
        
        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()
        time.sleep(10)

        
        # 5. Заполнение данных
        print("\nШаг 5: Заполнение данных")
        driver.find_element(By.ID, "first-name").send_keys("Иван")
        driver.find_element(By.ID, "last-name").send_keys("Петров")
        driver.find_element(By.ID, "postal-code").send_keys("123456")
        time.sleep(10)
        driver.find_element(By.ID, "continue").click()
        time.sleep(10)
        
        # 6. Завершение покупки
        print("\nШаг 6: Завершение покупки")
        driver.find_element(By.ID, "finish").click()
        time.sleep(10)
        
        # Проверка результата
        confirmation = driver.find_element(By.CLASS_NAME, "complete-header").text
        assert "Thank you for your order" in confirmation
        print("\n ТЕСТ УСПЕШНО ЗАВЕРШЕН \n")
        
    except Exception as e:
        print(f"\n ОШИБКА: {str(e)} ")
    finally:
        driver.quit()
        print("Браузер закрыт")

if __name__ == "__main__":
    test_purchase_flow()
