from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
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
    action = webdriver.common.action_chains.ActionChains(driver)
    action.move_by_offset(0, 0)
    action.click()
    action.perform()

    # Click 'All' in service requests
    xpath1 = "//html[@data-devicetype='doctype']/body/div/div/div/nav/div/div[@id='nav_west_center']/div/div/concourse-application-tree/ul/li[@id='concourse_application_7a1a14136fd64200a907c6012e3ee4b8']"

    xpath2 = "//html[@data-devicetype='doctype']/body/div/div/div/nav/div/div[@id='nav_west_center']/div/div/concourse-application-tree/ul/li[@id='concourse_application_7a1a14136fd64200a907c6012e3ee4b8']/ul/li[@id='concourse_module_471a14136fd64200a907c6012e3ee4bb']/div/ul/li/a"

    el = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath1)))
    el.click()
    anchor_all = driver.find_element_by_xpath(xpath2)
    anchor_all.click()


    ####
    # Load the MAIN frame
    wait.until(EC.frame_to_be_available_and_switch_to_it(driver.find_element_by_xpath("//html[@data-devicetype='doctype']/body/div/div/div/main/div/iframe")))


    # Click the HAMBURGER and magic
    list_control_btn = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//button[@data-original-title='List controls']")))
    list_control_btn.click()
    filter_item = driver.find_element_by_xpath("//div[@item_id='b17a69630a0a0bbb00f2601a9fa1e2da']")
    actions = ActionChains(driver)
    actions.move_to_element(filter_item).perform()
    pull_srqs = driver.find_element_by_xpath("//div[@item_id='sys_domainDYNAMIC429368b86f823100a907c6012e3ee41e^active=true^assignment_group=ed4bee396f976100a907c6012e3ee4a3^assigned_toISEMPTY^sys_updated_onONLast 7 days@javascript:gs.daysAgoStart(7)@javascript:gs.daysAgoEnd(0)^ORDERBYorder']")
    pull_srqs.click()
    # driver.switch_to.default_content()

    ####
    # Load the MAIN frame
    # wait.until(EC.frame_to_be_available_and_switch_to_it(driver.find_element_by_xpath("//html[@data-devicetype='doctype']/body/div/div/div/main/div/iframe")))
    
    table_header = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//table[@id='u_sc_request_table']/thead/tr[@id='hdr_u_sc_request']")))
    print(table_header)
    actions.move_to_element(table_header).context_click().perform()
    hover_on_export = driver.find_element_by_xpath("//div[@item_id='d1ad2f010a0a0b3e005c8b7fbd7c4e28']")
    actions.move_to_element(hover_on_export).perform()
    export_xlsx = driver.find_element_by_xpath("//div[@item_id='f13f0041473012003db6d7527c9a71f0']")
    export_xlsx.click()
    driver._switch_to.default_content()



except Exception as ex:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print(message)