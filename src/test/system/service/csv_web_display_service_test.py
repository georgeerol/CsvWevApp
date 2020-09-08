from app import app
from dev.mgr.display_mgr import DisplayCsvManager
from dev.model.csv_web_model import CsvWebAppCsvModel, CsvWebAppFileModel
from test.base_test import BaseTest


class CsvWebDisplayService(BaseTest):

    def test_display_service(self):
        filename = self.add_data()
        url_path = ('/csvwebapp/display/file/{}'.format(filename))
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
            display_mgr = DisplayCsvManager(filename)
            data = display_mgr.fetch_csv_data()
            actual_data = data['csv_data'][0]
            return filename
