from dev.model.csv_web_model import CsvWebAppFileModel


class DisplayManager:

    def __init__(self, filename):
        self.__filename = filename

    def fetch_csv_data(self):
        try:
            model = CsvWebAppFileModel.find_by_filename(self.__filename)
            dict_data = model.json()
            dict_data['message'] = 'Display {file} Successfully'.format(file=self.__filename)
            return dict_data
        except Exception as e:
            return {'message': " Error displaying csv {file}.".format(file=self.__filename) + str(e)}, 500
