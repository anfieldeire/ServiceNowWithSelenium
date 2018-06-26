from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import getpass

driver = webdriver.Firefox()
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

    vipLink = wait_until_clickable("vipOoblink", driver, 30)
    vipLink.click()

    sendOtpToPhone = wait_until_clickable("vipSend", driver, 5)
    sendOtpToPhone.click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "otpInput")))
    WebDriverWait(driver, 60).until(wait_for_text((By.ID, "otpInput")))
    vipSubmitOTP = driver.find_element_by_id("vipSubmitOTP")
    vipSubmitOTP.click()

except Exception as e:
    print(e)