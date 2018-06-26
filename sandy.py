from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.google.com")

class wait_for_text(object):
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        try:
            element_text = EC._find_element(driver, self.locator).get_attribute("value")
            print(element_text)
            return len(element_text) > 0
        except Exception as e:
            print(e)
            return False


WebDriverWait(driver, 20).until(wait_for_text((By.NAME, "q")))
driver.find_element_by_xpath("//input[@value='Search']").click()
