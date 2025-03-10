import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_5():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    all_links_page = driver.find_elements(By.TAG_NAME, "a")
    print(len(all_links_page))
    for i in all_links_page:
        print(i.text)

    time.sleep(5)
    driver.quit()
