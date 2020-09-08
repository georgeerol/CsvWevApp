from test.base_test import BaseTest
from dev.mgr.display_mgr import DisplayCsvManager
from dev.model.csv_web_model import CsvWebAppCsvModel
from dev.model.csv_web_model import CsvWebAppFileModel


class DisplayManagerTest(BaseTest):

    def test_fetch_csv_data(self):
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

            expected_data = {'age': age,
                             'date': date,
                             'email': email,
                             'first': first,
                             'guid': guid,
                             'last': last,
                             'name': name,
                             'phone': phone,
                             'state': state,
                             'street': street,
                             'value': value}

            csv_model = CsvWebAppCsvModel(guid, name, first, last, email, value, date, phone, age, state, street)
            file_model = CsvWebAppFileModel(filename, content_type, [csv_model])
            file_model.save_to_db()
            display_mgr = DisplayCsvManager(filename)
            data = display_mgr.fetch_csv_data()
            actual_data = data['csv_data'][0]
            self.assertEqual(filename, data['filename'])
            self.assertEqual(expected_data, actual_data)
