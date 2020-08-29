from dev.util.yaml.yaml import load_yaml

"""
AppSetup

This class needs to be called to get information from the config.yaml file
"""


class AppSetup:

    def __init__(self, config_path="config/config.yaml"):
        self.config_path = config_path

    def init(self, env="dev"):
        if env == "prod":
            # Add prod config file
            pass
        elif env == "dev":
            load_yaml(self.config_path)
        else:
            load_yaml(self.config_path)
