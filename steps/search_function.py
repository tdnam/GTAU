from cgi import test
from distutils.command.config import config
from behave import *
import pages.search_page as search_page
import configReader


@given('user accesses Gumtree')
def access_page(context):
    try:
        search_page.navigate_to_url(configReader.settings["url"])
    except:
        raise Exception("Failed to navigate to url.")


@when('user searches for "{search_keyword}" with catergory "{search_category}", distance "{search_distance}" and area "{search_area}"')
def search_for(context, search_keyword, search_category, search_distance, search_area):
    try:
        search_page.search_for(search_keyword, search_category, search_distance, search_area)
    except:
        raise Exception("Failed during entering searching parameters.")


@when('user opens a random result')
def open_a_random_search_result(context):
    try:
        search_page.open_a_random_search_result()
    except:
        raise Exception("Failed to open a random search result")


@then('user verifies the ad details page open')
def verify_details_page_open_after_search(context):
    search_page.verify_details_page_open_after_search()


@then('user ensures a numeric ad id is displayed in the breadcrumbs and verify at least one similar ad is displayed in the page')
def verify_numeric_ad_id_and_similar_ad(context):
    search_page.verify_numeric_ad_id_and_similar_ad()