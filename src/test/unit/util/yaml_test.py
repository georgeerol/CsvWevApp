from unittest import TestCase
from dev.util.yaml.yaml import load_yaml, get_yaml


class YamlConfigTest(TestCase):

    def test_load_yaml(self):
        config_path = 'config/config.yaml'
        test = load_yaml(config_path)
        self.assertEqual(None, test)

    def test_load_yaml_wrong_path(self):
        config_path = 'config/test.yaml'
        with self.assertRaises(Exception):
            load_yaml(config_path)

    def test_get_yaml_wrong_key(self):
        key = 'url_key'
        with self.assertRaises(Exception):
            get_yaml(key)
