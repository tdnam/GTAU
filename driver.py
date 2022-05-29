from selenium import webdriver
import configReader
import os

instance = None

def initialize():
    global instance
    if configReader.settings["browser"] == "chrome":
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--ignore-ssl-errors')
        chrome_options.add_experimental_option("prefs", prefs)
        instance = webdriver.Chrome(executable_path=os.getcwd()+"/lib/chromedriver", chrome_options=chrome_options)
        instance.maximize_window()
        instance.implicitly_wait(configReader.settings["implicit_wait_secs"])
    else:
        raise Exception("Failed to initialise driver")


def stop_instance():
    instance.quit()


def close_browser():
    instance.close()


def clear_cookies():
    instance.delete_all_cookies()


def get_current_url():
    return instance.current_url


def navigate(url):
    instance.get(url)
    set_first_chrome_tab_handle()


def switch_to_frame(frame_name):
    instance.switch_to.frame(instance.find_element_by_name(frame_name))
    

def switch_to_frame_by_id(frame_id):
    instance.switch_to.frame(instance.find_element_by_id(frame_id))


def switch_to_default_content():
    instance.switch_to.default_content()


def close_current_tab():
    instance.close()


def set_first_chrome_tab_handle():
    global FIRST_CHROME_TAB_HANDLE
    FIRST_CHROME_TAB_HANDLE = instance.current_window_handle


def get_first_chrome_tab_handle():
    return FIRST_CHROME_TAB_HANDLE


def get_current_chrome_tab_handle():
    return instance.current_window_handle


def get_window_size():
    return instance.get_window_size()


def find_element(by_strategy, locator):
    return instance.find_element(by_strategy, locator)


def find_elements(by_strategy, locator):
    return instance.find_elements(by_strategy, locator)


def find_element_by_xpath(locator):
    return instance.find_element_by_xpath(locator)