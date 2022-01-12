import random

import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

options = Options()
options.add_argument('--headless')# ヘッドレスモードで実行する(Windowが生成されないからディスプレイがない環境でもできる)

driver = webdriver.Chrome() # https://github.com/actions/virtual-environments/blob/main/images/linux/Ubuntu2004-Readme.md にかいてあるっぽい

url = f"https://docs.google.com/forms/d/e/1FAIpQLSdYD-mLD2ILW9m7mLy-TqtmuFlt2lTP_jbRosNC7BP0zNesWA/viewform?usp=pp_url&entry.925303296={random.randint(360,366)/10}" # 360~366までの乱数(整数)を10で割って入れる

driver.get(url)
email_address = "61229liu@seiko.ac.jp"
with open("./password.txt") as f:
    password = f.read()# パスワードをファイルから読み込む
# driver.save_screenshot("a.png")
# html=driver.find_element_by_css_selector("html")
# print(html.get_attribute('innerHTML'))
email = driver.find_element_by_css_selector("#Email")
email.send_keys(email_address)
email.send_keys(Keys.ENTER)
wait = WebDriverWait(driver, 10)  # waitインスタンスを作る
# time.sleep(10)
# driver.save_screenshot("b.png")
# html=driver.find_element_by_css_selector("html")
# print(html.get_attribute('innerHTML'))
wait.until(expected_conditions.presence_of_element_located(
    (By.CSS_SELECTOR, "input[type=\"password\"]")))  # パスワードの画面が読み込まれるまで待つ
password_element = driver.find_element_by_css_selector(
    "input[type=\"password\"]")
password_element.send_keys(password)
# password_element.send_keys(Keys.ENTER)
wait.until(expected_conditions.presence_of_element_located(
    (By.CSS_SELECTOR, "span.freebirdFormviewerViewHeaderEmailAddress")))  # フォーム画面が読み込まれるまで待つ
send_button = driver.find_element_by_css_selector("div[role=\"button\"]")
send_button.click()
wait.until(expected_conditions.presence_of_element_located(
    (By.CSS_SELECTOR, "div.freebirdFormviewerViewResponseConfirmationMessage")))  # 終了画面が読み込まれるまで待つ

driver.close()
driver.quit()
