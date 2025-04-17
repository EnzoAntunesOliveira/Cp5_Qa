from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "http://localhost:3003"
USERNAME = "admin"
PASSWORD = "password"

def test_login_success():
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.find_element(By.ID, "username").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "doLogin").click()
    time.sleep(2)
    assert "Welcome" in driver.page_source
    driver.quit()

def test_login_failure():
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.find_element(By.ID, "username").send_keys("wronguser")
    driver.find_element(By.ID, "password").send_keys("wrongpass")
    driver.find_element(By.ID, "doLogin").click()
    time.sleep(2)
    assert "Login failed" in driver.page_source
    driver.quit()
