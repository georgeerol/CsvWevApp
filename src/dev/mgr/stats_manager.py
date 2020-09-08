from dev.model.csv_web_model import CsvWebAppCsvModel


class PeopleStatsManager:

    def __init__(self, filename):
        self.__filename = filename

    def get_persons_per_year(self):
        try:
            years = CsvWebAppCsvModel.get_year_list(self.__filename)
            people_in_year_list = []
            for year in years:
                num_of_person = CsvWebAppCsvModel.get_people_sum(self.__filename, year)
                people_in_year = PeopleInYear(year, num_of_person[0])
                people_in_year_list.append(people_in_year.json())
            message = 'Fetch Stats {file} Successfully.'.format(file=self.__filename)
            return {'message': message, 'filename': self.__filename,'persons_per_year': people_in_year_list}
        except Exception as e:
            return {'message': " Error with {file}.".format(file=self.__filename) + str(e)}, 500


class PeopleInYear:

    def __init__(self, year, person):
        self.__year = year
        self.__person = person

    def json(self):
        return {'year': self.__year, 'person': self.__person}
