from selenium import webdriver


def test_open_vwo_login():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    print(driver.title)
    assert driver.title == "Login - VWO"
