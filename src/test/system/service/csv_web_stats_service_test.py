from app import app
from dev.model.csv_web_model import CsvWebAppCsvModel
from test.base_test import BaseTest


class CsvWebStatisticsService(BaseTest):

    def test_stats_service(self):
        filename = self.add_data()
        url_path = ('/csvwebapp/statistics/file/{}'.format(filename))
        with app.test_client() as c:
            resp = c.get(url_path, query_string={'filename': filename})
            self.assertEqual(200, resp.status_code)

    def add_data(self):
        with self.app_context():
            guid = '1234'
            filename_id = 'test.csv'
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
            model = CsvWebAppCsvModel(guid, name, first, last, email, value, date, phone, age, state, street)
            model.filename_id = filename_id
            model.save_to_db()
            return filename_id
