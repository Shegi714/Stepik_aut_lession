from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import  time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной


wait_price = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR,'div > #price'),"$100")
    )
button = browser.find_element(By.CSS_SELECTOR,'div > #book')
button.click()

x_element = browser.find_element(By.XPATH,'//*[@id="input_value"]')
x = x_element.text
y = calc(x)

input1 = browser.find_element(By.CSS_SELECTOR, 'div > #answer' )
input1.send_keys(y)

button2 = browser.find_element(By.XPATH,'//*[@id="solve"]')
browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
button2.click()

time.sleep(20)

alert2 = browser.switch_to.alert
alert_text = alert2.text
print(alert_text)
