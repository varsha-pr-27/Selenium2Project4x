import time

import pytest
from selenium import webdriver


class TestSelenium:
    def __init__(self):
        self.driver = None

    def open_browser(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--incognito")

        self.driver = webdriver.Chrome(self.chrome_options)
        self.driver.get("https://selectorshub.com/xpath-practice-page/")
        self.driver.maximize_window()

    @pytest.mark.smoke
    def test_js(self):
        title = self.driver.execute_script("return document.title")
        current_url = self.driver.execute_script("return document.URL")
        print(current_url)
        print(title)
        assert current_url == "https://selectorshub.com/xpath-practice-page/"

    def close_browser(self):
        time.sleep(3)  # Wait for 3 seconds before closing
        self.driver.quit()


test = TestSelenium()
test.open_browser()
test.test_js()
test.close_browser()
