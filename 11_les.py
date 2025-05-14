from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)


    input1 = browser.find_element(By.CSS_SELECTOR,'[name="firstname"]')
    input1.send_keys("kuku")

    input2 = browser.find_element(By.CSS_SELECTOR,'[name="lastname"]' )
    input2.send_keys("epta")

    input3 = browser.find_element(By.CSS_SELECTOR,'[name="email"]')
    input3.send_keys("chirik@eba.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "test.txt")
    input4 = browser.find_element(By.CSS_SELECTOR,'form > #file' )
    input4.send_keys(file_path)

    input5 = browser.find_element(By.CSS_SELECTOR, 'form > button')
    input5.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()