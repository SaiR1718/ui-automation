import pytest
from selenium import webdriver

@pytest.mark.sanity
def test_home_page_load():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()