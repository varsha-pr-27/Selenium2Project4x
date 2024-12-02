import allure
from selenium import webdriver


@allure.title("Verify the title of the webpage testing_academy.com")
def test_sample():
    driver = webdriver.Chrome()
    driver.get("https://sdet.live")

    driver = webdriver.Edge()
    driver.get("https://google.com")
    assert driver.current_url == "https://www.google.com/"
