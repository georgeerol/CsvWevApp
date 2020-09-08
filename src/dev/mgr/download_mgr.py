import os
import csv
from dev.model.csv_web_model import CsvWebAppFileModel
from dev.util.helper.get_config import get_config_value


class DownloadCsvManager:

    def __init__(self, filename):
        self.__filename = filename
        self.csv_columns = []
        self.dict_data = {}

    def prepare_csv_file(self):
        self.__find_file()
        path = get_config_value('temp_download_folder')
        if not os.path.exists(path):
            os.makedirs(path)
        csv_file = self.__filename
        try:
            with open(os.path.join(path, csv_file), 'w+') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.csv_columns)
                writer.writeheader()
                for data in self.dict_data['csv_data']:
                    writer.writerow(data)
        except IOError as e:
            return {'message': str(e)}, 500
        return {'message': 'Done'}

    def __find_file(self):
        try:
            model = CsvWebAppFileModel.find_by_filename(self.__filename)
            self.dict_data = model.json()
            self.csv_columns = self.dict_data['csv_data'][0].keys()
        except Exception as e:
            return {'message': str(e)}, 500
