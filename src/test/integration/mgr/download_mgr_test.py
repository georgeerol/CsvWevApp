import os
from test.base_test import BaseTest
from dev.mgr.download_mgr import DownloadCsvFileManager
from dev.model.csv_web_model import CsvWebAppCsvModel
from dev.model.csv_web_model import CsvWebAppFileModel
from dev.util.helper.get_config import get_config_value


class DownloadCsvFileManagerTest(BaseTest):

    def test_process_file(self):
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
            download_mgr = DownloadCsvFileManager(filename)
            download_mgr_msg = download_mgr.prepare_csv_file()
            self.assertEqual({'message': 'Done'}, download_mgr_msg)
            os.remove(get_config_value('temp_download_folder') + '/' + filename)
