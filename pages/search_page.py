import driver
import common.common as common
import configReader as config
from objects.locator import GenericObject, SearchPage, AdDetailsPage


def navigate_to_url(url):
    driver.navigate(url)


def search_for(search_keyword, search_category, search_distance, search_area):
    #keyword
    common.clear_and_type_text_on_element(GenericObject.input_with_placeholder_contains, "looking for", text=search_keyword)
    
    #category
    common.click_element(GenericObject.input_with_id_contains, "categoryId")
    common.wait_until_element_exists(GenericObject.div_with_text_equals, config.settings["explicit_wait_secs"], search_category)
    common.click_element_js(GenericObject.div_with_text_equals, search_category)
    
    #distance
    common.click_element(GenericObject.div_with_data_list_contents_contains, "radiuses")
    common.wait_until_element_exists(GenericObject.div_with_text_equals, config.settings["explicit_wait_secs"], search_distance)
    common.click_element_js(GenericObject.div_with_text_equals, search_distance)

    #area
    common.clear_and_type_text_on_element(GenericObject.input_with_id_contains, "search-area", text=search_area)

    #click search
    common.click_element(GenericObject.button_with_class_equals, "header__search-button")
    common.wait_until_element_exists(GenericObject.h1_with_text_contains, config.settings["explicit_wait_secs"], " Results: ")


def open_a_random_search_result():
    common.wait_until_element_exists(SearchPage.first_search_result, config.settings["explicit_wait_secs"])
    common.click_element(SearchPage.first_search_result)


def verify_details_page_open_after_search():
    expected_attrubute_items = ["Date Listed:", "Last Edited:", "Condition:", "Shipping:"]
    number_of_attribute_items = common.count_all_elements(AdDetailsPage.ad_attribute_items)

    if number_of_attribute_items > 0:
        for i in range(1, number_of_attribute_items+1):
            ui_add_attribute = common.get_element_value(AdDetailsPage.ad_attribute_item, str(i))
            if ui_add_attribute not in expected_attrubute_items:
                print("ERROR: {0} is not in the attribute items".format(ui_add_attribute))
                raise
    else:
        print("ERROR: ad details page seems not open correctly")
        raise


def verify_numeric_ad_id_and_similar_ad():
    ad_id = common.get_element_value(AdDetailsPage.ad_id)
    ad_id = ad_id.replace("Ad ID ", "")
    if not ad_id.isnumeric():
        print("ERROR: Ad id {0} is not numberic or not found!".format(ad_id))
        raise

    #Similar ad
    number_of_similar_ads = common.count_all_elements(AdDetailsPage.similar_ads)
    if int(number_of_similar_ads) < 1:
        print("ERROR: The number of similar ads is {0}. There should be at least 1 similar ad displayed".format(number_of_similar_ads))
    