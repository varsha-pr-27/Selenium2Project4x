from selenium import webdriver


def test_open_vwo_login():
    driver = webdriver.Chrome()  # Create session
    driver.get("https://app.vwo.com")  # Navigate to the url
    page_source_data = driver.page_source  # Find the page source
    print(page_source_data)
