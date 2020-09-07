import os
from test.base_test import BaseTest
from dev.mgr.get_files_mgr import GetCsvFilesManager
from dev.model.csv_web_model import CsvWebAppCsvModel
from dev.model.csv_web_model import CsvWebAppFileModel


class GetCsvFilesManagerTest(BaseTest):

    def test_get_csv_files(self):
        with self.app_context():
            content_type = 'text/csv'
            guid = '1234'
            expected_filename = 'test.csv'
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

            expected_url = "http://{host}:{port}/csvwebapp/files/{filename}".format(host=os.getenv('app_host'),
                                                                                    port=os.getenv('app_port'),
                                                                                    filename=expected_filename)
            csv_model = CsvWebAppCsvModel(guid, name, first, last, email, value, date, phone, age, state, street)
            file_model = CsvWebAppFileModel(expected_filename, content_type, [csv_model])
            file_model.save_to_db()
            get_files_mgr = GetCsvFilesManager()
            csv_files = get_files_mgr.get_csv_files()
            actual_filename = csv_files[0]['name']
            self.assertEqual(expected_filename, actual_filename)
            self.assertEqual(expected_url, csv_files[0]['url'])
