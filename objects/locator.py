
from selenium.webdriver.common.by import By

class Locator:
    def __init__(self, type, selector) -> None:
        self.type = type
        self.selector = selector

    def format_locator(self, *args):
        return self.selector.format(*args)


class SearchPage:
    first_search_result = Locator(By.XPATH, "(//p[@class='user-ad-row-new-design__title'])[1]")


class AdDetailsPage:
    ad_attribute_items = Locator(By.XPATH, "//div[@class='vip-ad__container']//div[@class='vip-ad-attributes']//span[@class='vip-ad-attributes__value']")
    ad_attribute_item = Locator(By.XPATH, "(//div[@class='vip-ad__container']//div[@class='vip-ad-attributes']//span[@class='vip-ad-attributes__value'])[{0}]")
    ad_id = Locator(By.XPATH, "//span[@class='breadcrumbs__summary']")
    similar_ads = Locator(By.XPATH, "//div[text()='Similar Ads']/parent::div//div[@class='panel-body vip-similar-ads__slider-container']//li")


class GenericObject:
    input_with_placeholder_contains = Locator(By.XPATH, "//input[contains(@placeholder, '{0}')]")
    input_with_id_contains = Locator(By.XPATH, "//input[contains(@id, '{0}')]")
    div_with_text_equals = Locator(By.XPATH, "//div[text()='{0}']")
    div_with_data_list_contents_contains = Locator(By.XPATH, "//div[contains(@data-list-contents, '{0}')]")
    button_with_class_equals = Locator(By.XPATH, "//button[@class='{0}']")
    h1_with_text_contains = Locator(By.XPATH, "//h1[contains(text(), '{0}')]")