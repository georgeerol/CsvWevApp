from test.base_test import BaseTest
from dev.mgr.stats_manager import PeopleStatsManager
from dev.model.csv_web_model import CsvWebAppCsvModel


class PeopleStatsManagerTest(BaseTest):

    def test_get_persons_per_year(self):
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
            stats = PeopleStatsManager(filename_id)
            data = stats.get_persons_per_year()
            self.assertEqual(filename_id, data['filename'])
            self.assertEqual({'person': 1, 'year': 2018}, data['persons_per_year'][0])
