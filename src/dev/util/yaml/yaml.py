import yaml

yaml_dict = {}


def load_yaml(config_path):
    '''
    Load configuration settings file
    :return:
    '''
    with open(config_path, 'r') as stream:
        try:
            global yaml_dict
            yaml_dict = yaml.load(stream, Loader=yaml.SafeLoader)
        except yaml.YAMLError as exc:
            print(exc)


def get_yaml(key):
    """
    Get the configuration settings for processing
    :param key:
    :return:
    """
    if len(yaml_dict) != 0 and key in yaml_dict:
        return yaml_dict[key]
    else:
        raise Exception("Unable to get yaml config information or key value ")
