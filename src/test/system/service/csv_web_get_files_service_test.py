import os
from app import app
from dev.mgr.get_files_mgr import GetCsvFilesManager
from dev.model.csv_web_model import CsvWebAppCsvModel
from dev.model.csv_web_model import CsvWebAppFileModel
from dev.util.helper.get_config import get_config_value
from test.base_test import BaseTest


class CsvWebGetFilesService(BaseTest):

    def test_get_files_service(self):
        self.add_data()
        url_path = get_config_value('get_list_of_files')
        with app.test_client() as c:
            resp = c.get(url_path)
            self.assertEqual(200, resp.status_code)

    def add_data(self):
        with self.app_context():
            content_type = 'text/csv'
            guid = '1234'
            filename = 'test.csv'
            name = 'Eddie Glover'
            first = 'Frank'
            last = 'Guerrero'
            email = 'abc@bc.com'
            value = 'value'
            date = '2/19/2018'
            phone = '1234567'
            age = '100'
            state = 'NY'
            street = "ST. Patrick"

            csv_model = CsvWebAppCsvModel(guid, name, first, last, email, value, date, phone, age, state, street)
            file_model = CsvWebAppFileModel(filename, content_type, [csv_model])
            file_model.save_to_db()
            get_files_mgr = GetCsvFilesManager()
            get_files_mgr.get_csv_files()
            return filename
