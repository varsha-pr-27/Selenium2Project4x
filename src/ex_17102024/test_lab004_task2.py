# Create a Selenium Script to verify the title for
# Open the Page - https://katalon-demo-cura.herokuapp.com/
# Verify the current URL, current title
# In the page source add a assertion that “CURA Healthcare Service” exist in the page.
# driver.pageSource() - String

from selenium import webdriver


def test_task2():
    driver = webdriver.Chrome()  # Create session
    driver.get("https://katalon-demo-cura.herokuapp.com/")  # Navigate to the url
    page_source_data = driver.page_source  # Find the page source
    print(page_source_data)
    assert "CURA Healthcare Service" in page_source_data
    driver.quit()
