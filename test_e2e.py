from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_purchase_flow():
    # Настройка драйвера
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 15)
    
    try:
        print("\nТЕСТ НАЧИНАЕТСЯ\n")
        
        # 1. Авторизация
        print("Шаг 1: Авторизация")
        driver.get("https://www.saucedemo.com/")
        time.sleep(2)  # Краткая пауза для стабильности
        
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)  # Ожидание перехода
        
        # 2. Добавление товара
        print("\nШаг 2: Добавление товара")
        wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
        time.sleep(2)
        
        # 3. Проверка корзины
        print("\nШаг 3: Проверка корзины")
        try:
            cart_badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
            print(f"Товаров в корзине: {cart_badge.text}")
        except:
            print("Элемент shopping_cart_badge не найден, проверяем альтернативно...")
            driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
            try:
                item = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name")))
                print(f"В корзине: {item.text}")
            except:
                raise Exception("Товар не добавился в корзину")
        
        # 4. Оформление заказа (ключевое изменение)
        print("\nШаг 4: Оформление заказа")
        driver.get("https://www.saucedemo.com/cart.html")
        time.sleep(2)  # Важно для стабильности
        
        # Явная проверка кнопки Checkout
        checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()
        time.sleep(2)
        
        # 5. Заполнение данных
        print("\nШаг 5: Заполнение данных")
        wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Володя")
        driver.find_element(By.ID, "last-name").send_keys("Володин")
        driver.find_element(By.ID, "postal-code").send_keys("123456")
        time.sleep(1)
        driver.find_element(By.ID, "continue").click()
        time.sleep(2)
        
        # 6. Завершение покупки (с дополнительными проверками)
        print("\nШаг 6: Завершение покупки")
        try:
            finish_button = wait.until(
                EC.element_to_be_clickable((By.ID, "finish")),
                message="Кнопка Finish не найдена после 15 секунд ожидания"
            )
            finish_button.click()
            
            # Проверка результата
            confirmation = wait.until(
                EC.text_to_be_present_in_element((By.CLASS_NAME, "complete-header"), "Thank you for your order"),
                message="Подтверждение заказа не появилось"
            )
            print("\nТЕСТ УСПЕШНО ЗАВЕРШЕН\n")
            
        except Exception as e:
            print(f"\nОШИБКА НА ЭТАПЕ ЗАВЕРШЕНИЯ: {str(e)}")
            driver.save_screenshot("checkout_error.png")
            raise
        
    except Exception as e:
        print(f"\nОШИБКА: {str(e)}")
        driver.save_screenshot("general_error.png")
        raise
    finally:
        driver.quit()
        print("Браузер закрыт")

if __name__ == "__main__":
    test_purchase_flow()
