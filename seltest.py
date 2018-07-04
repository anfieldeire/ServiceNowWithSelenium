from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import getpass

driver = webdriver.Firefox()
# Implicitly wait 30 seconds to find elements in DOM
driver.get("https://afsitsm.service-now.com")

def wait_until_clickable(element, driver, time):
    return WebDriverWait(driver, time).until(EC.element_to_be_clickable((By.ID, element)))

class wait_for_text(object):
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        element_text = EC._find_element(driver, self.locator).get_attribute("value")
        print(element_text)
        return len(element_text) == 6

try:
    # Enter credentials and go to service now
    username = driver.find_element_by_id("userNameInput")
    password = driver.find_element_by_id("passwordInput")

    username.send_keys("nilabjo.sanyal")
    password.send_keys("san$$yal@@94", Keys.RETURN)

    home_url = 'https://afsitsm.service-now.com/nav_to.do?uri=%2Fhome.do%3F'

    wait = WebDriverWait(driver, 120)
    wait.until(lambda driver: driver.current_url == home_url)

    print("Reached service now!")

    # Click 'All' in service requests
    anchor_all = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='471a14136fd64200a907c6012e3ee4bb']")))
    anchor_all.click()

except Exception as e:
    print(e)