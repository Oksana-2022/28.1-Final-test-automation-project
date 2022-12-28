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

def test_telephon_present():
   '''Проверяем, что на странице присутствет Таб выбора аутентификации "Телефон"'''
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "Телефон")))
   pytest.driver.find_element(By.name, 'Телефон')

