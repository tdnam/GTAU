import yaml
import os

settings = None

def load_settings_for_environment(environment):
    global settings
    with open(os.path.join(os.path.dirname(__file__), 'config.yaml')) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        settings = data[environment]