from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
  link = "http://suninjuly.github.io/execute_script.html"
  browser = webdriver.Chrome()
  browser.get(link)

  x_element = browser.find_element(By.CSS_SELECTOR, 'label > #input_value')
  x = x_element.text
  y = calc(x)

  input1 = browser.find_element(By.CSS_SELECTOR, 'div > #answer')
  browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
  input1.send_keys(y)

  input2 = browser.find_element(By.CSS_SELECTOR, 'div > #robotCheckbox')
  browser.execute_script("return arguments[0].scrollIntoView(true);", input2)
  input2.click()
  input3 = browser.find_element(By.CSS_SELECTOR, 'div > #robotsRule')
  browser.execute_script("return arguments[0].scrollIntoView(true);", input3)
  input3.click()

  input4 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
  browser.execute_script("return arguments[0].scrollIntoView(true);", input4)
  input4.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()