import driver
import configReader
import logging

def before_step(context, step):
    pass

def after_step(context, step):
    pass

def before_scenario(context, scenario):
    driver.initialize()

def after_scenario(context, scenario):
    driver.close_browser()

def before_feature(context, feature):
    pass

def after_feature(context, feature):
    pass

def before_tag(context, tag):
    pass

def after_tag(context, tag):
    pass

def before_all(context):
    configReader.load_settings_for_environment("DEV")
    logging.getLogger().setLevel(logging.INFO)
    print("Configuration has been loaded")

def after_all(context):
    driver.stop_instance()
