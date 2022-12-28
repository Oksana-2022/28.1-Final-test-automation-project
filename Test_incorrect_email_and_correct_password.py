import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('C:/chromedriver1/chromedriver1.exe')

   # Переходим на страницу авторизации
   pytest.driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope=openid&state=c5c58aa1-47fe-4e6f-b822-286792942d2f&theme=light&auth_type')
   yield
   pytest.driver.quit()

def test_incorrect_email_and_correct_password():
   '''Проверяем авторизацию на странице с некорректным email и корректным паролем.'''

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.ID, "t-btn-tab-mail")))
   # Нажимаем на Tab "Почта"
   pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
   # Вводим некорректный email
   pytest.driver.find_element(By.ID, 'username').send_keys('egunova-a@mail.ru')

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
   # Вводим корректный пароль
   pytest.driver.find_element(By.ID, 'password').send_keys('Anna-Maria.2020')

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "form-error-message")))
   # Проверяем, что в личном кабинете присутствует надпись "Неверный логин или пароль".
   pytest.driver.find_element(By.ID, 'form-error-message')