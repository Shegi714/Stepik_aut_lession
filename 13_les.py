from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

time.sleep(2)

button3 = browser.find_element(By.CSS_SELECTOR,'div > button')
button3.click()

time.sleep(1)

all_window = browser.window_handles
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

time.sleep(1)

#button1 = browser.find_element(By.CSS_SELECTOR,'div > button')
#button1.click()

#alert = browser.switch_to.alert
#alert.accept()




x_element = browser.find_element(By.XPATH,'//*[@id="input_value"]')
x = x_element.text
y = calc(x)


input1 = browser.find_element(By.CSS_SELECTOR, 'div > #answer' )
input1.send_keys(y)

button2 = browser.find_element(By.CSS_SELECTOR,'div > button')
button2.click()

time.sleep(2)

alert2 = browser.switch_to.alert
alert_text = alert2.text
print(alert_text)



