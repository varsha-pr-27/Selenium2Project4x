# Open the Url - www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067
# Search for the Macmini
# Click on the search ICON
# Get all the titles
# Get al the prices
# Print all the titles and prices in the end. (side by side)
# Find the Max and Min price also (from the list)


import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.title("Print the Titles of the Ebay sites after searching")
@allure.description("Verify that 62 items are there for macmini")
def test_5():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")

    search_box_input_xpath = driver.find_element(By.XPATH, "//input[@placeholder='Search for anything']")
    # search_box_inout_css = driver.find_element(By.CSS_SELECTOR,"#gh-ac")
    search_box_input_xpath.send_keys("macmini")

    search_box_button = driver.find_element(By.CSS_SELECTOR, "button[value='Search']")
    search_box_button.click()

    list_of_items = driver.find_elements(By.CSS_SELECTOR, ".s-item__title")
    list_of_items_prize = driver.find_elements(By.CSS_SELECTOR, ".s-item__price")
    j = 0
    for i in list_of_items:
        print(i.text, "-->", list_of_items_prize[j].text)
        j = j + 1

    time.sleep(5)
    driver.quit()
