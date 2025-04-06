import os
import json


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def load_config():
    """
    Load the configuration file and return the config object.
    """


    config_path = os.path.join(os.path.dirname(__file__),"..", 'config.json')
    print(f"{bcolors.OKGREEN}Loading configuration from {config_path}{bcolors.ENDC}")
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    return config