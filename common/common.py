import time
import logging
import configReader as config
import driver as driver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from objects.locator import GenericObject


def _execute_with_wait(condition):
    return WebDriverWait(driver.instance, config.settings["explicit_wait_secs"]).until(condition)


def wait_for_element(locator):
    _execute_with_wait(ec.element_to_be_clickable(locator.type, locator.selector))


def wait_until_element_exists(locator, timeout_secs, *selector_params):
    WebDriverWait(driver.instance, timeout_secs).until(ec.presence_of_element_located((locator.type, format_locator(locator, *selector_params))))


def wait_until_element_disappears(locator, timeout_secs, *selector_params):
    if len(selector_params) > 0:
        selector = locator.format_selector(*selector_params)
    else:
        selector = locator.selector
    WebDriverWait(driver.instance, timeout_secs).until(ec.invisibility_of_element_located((locator.type, selector)))


def wait_for_items_to_load():
    try:
        if (driver.instance.find_element("xpath", "//span[text()='Loading menu items...']").is_displayed()) == True:
            time.sleep(30)
    except:
        print("All items loaded")


def count_all_elements(locator, *selector_params):
    selector = format_locator(locator, *selector_params)
    return len(driver.instance.find_elements(locator.type, selector))


def element_exists(locator):
    try:
        time.sleep(1)
        _execute_with_wait(ec.presence_of_element_located((locator.type, locator.selector)))
        return True
    except TimeoutException:
        return False


def multi_select_for_dynamic_element(main_element,option_to_select):
    ActionChains(driver.instance).move_to_element(driver.instance.find_element_by_xpath("//div[text()='"+main_element+"']/following-sibling::div//li//span[contains(text(),'"+option_to_select+"')]")).click().perform()


def element_is_checked(locator, *selector_params):
    return driver.find_element(locator.type, format_locator(locator, *selector_params)).is_selected()


def click_element(locator, *selector_params):
    selector = format_locator(locator, *selector_params)
    try:
        driver.instance.execute_script("arguments[0].click();", driver.instance.find_element(locator.type, selector))
    except:
        logging.error("Click element by executing Javascript {0} is not working".format(format(str(locator.selector))))


def click_element_js(locator, *selector_params):
    try:
        driver.find_element(locator.type, format_locator(locator, *selector_params)).click()
    except:
        logging.error("Click element by default {0} is not working".format(format(str(locator.selector))))
        

def type_text_on_element(locator, *selector_params, text):
    try:
        driver.find_element(locator.type, format_locator(locator, *selector_params)).send_keys(text)
    except:
        logging.error("Type text on element {0} is not working".format(format(str(locator.selector))))


def type_text_on_element_then_press_enter(locator, *selector_params, text):
    try:
        driver.find_element(locator.type, format_locator(locator, *selector_params)).send_keys(text)
        ActionChains(driver.instance).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    except:
        logging.error("Type text on element {0} then press enter is not working".format(format(str(locator.selector)))) 
 
 
def press_key(key):
    try:
        ActionChains(driver.instance).key_down(key).key_up(key).perform()
    except:
       logging.error("Press key is not working.") 
 

def clear_and_type_text_on_element(locator, *selector_params, text):
    try:
        element = driver.find_element(locator.type, format_locator(locator, *selector_params))
        driver.find_element(locator.type, format_locator(locator, *selector_params)).send_keys(text)
    except:
        import traceback
        print(traceback.print_exc())
        logging.error("Clear and type text on element {0} is not working".format(str(locator.selector)))

        
def clear_text_on_element(locator, *selector_params):
    try:
        driver.find_element(locator.type, format_locator(locator, *selector_params)).clear()
    except:
        logging.error("Clear text on element {0} is not working".format(str(locator.selector)))


def clear_text_on_element_by_keyboard(locator, *selector_params):
    try:
        ActionChains(driver.instance).key_down(Keys.CONTROL).send_keys('a').perform()
        ActionChains(driver.instance).send_keys(Keys.DELETE).perform()
    except:
        logging.error("Clear text on element {0} using keyboard is not working".format(str(locator.selector)))
  
        
def element_is_present(locator, *selector_params):
    return len(driver.find_elements(locator.type, format_locator(locator, *selector_params))) > 0


def element_not_present(locator, *selector_params):
    return len(driver.find_elements(locator.type, format_locator(locator, *selector_params))) == 0


def get_element_value(locator, *selector_params):
    return driver.find_element(locator.type, format_locator(locator, *selector_params)).text


def get_attribute_value(locator, *selector_params, attribute_name="value"):
    return (driver.find_element(locator.type, format_locator(locator, *selector_params))).get_attribute(attribute_name)


def upload_file(locator, *selector_params, file_path, hidden_upload=False, element_id):
    if hidden_upload:
        try:
            driver.instance.execute_script("document.getElementById('{0}').style.visibility='visible'".format(element_id))
        except:
            logging.warn("Execute Javascript failed. Element may be not hidden")
    driver.find_element(locator.type, format_locator(locator, *selector_params)).send_keys(file_path)
    

def format_locator(locator, *selector_params):
    if len(selector_params) > 0:
        return locator.format_locator(*selector_params)
    else:
        return locator.selector


def wait_for_loading_spinner():
    ''' Wait for the loading spinner to complete/disappear '''
    wait_until_element_disappears(GenericObject.loading_spinner, 15)


def refresh_page():
    driver.instance.refresh()


def scroll_to_element(locator, *selector_params):
    driver.instance.execute_script("arguments[0].scrollIntoView(true)", format_locator(locator, *selector_params))