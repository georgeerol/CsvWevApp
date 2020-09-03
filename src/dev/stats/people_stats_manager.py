from dev.model.csv_web_model import CsvWebAppCsvModel
from dev.stats.people_in_year import PeopleInYear


class PeopleStatsManager:

    def __init__(self, filename):
        self.filename = filename
        pass

    def get_persons_per_year(self):
        years = CsvWebAppCsvModel.get_year_list(self.filename)
        people_in_year_list = []
        for year in years:
            num_of_person = CsvWebAppCsvModel.get_people_sum(self.filename, year)
            people_in_year = PeopleInYear(year, num_of_person[0])
            people_in_year_list.append(people_in_year.json())
        return {'filename': self.filename, 'stats_data': people_in_year_list}
