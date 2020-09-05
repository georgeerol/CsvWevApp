import csv
import io
from dev.model.csv_web_model import CsvWebAppFileModel, CsvWebAppCsvModel


class UploadManager:

    def __init__(self, file):
        self.__file = file
        self.__filename = None
        self.__content_type = None
        self.__data_list = []

    def save_to_db(self):
        self.__get_data_from_file()
        try:
            model = CsvWebAppFileModel(self.__filename, self.__content_type, self.__data_list)
            model.save_to_db()
            return {'message': 'Upload {file} Successfully'.format(file=self.__filename)}, 201
        except Exception as e:
            return {'message': " Error  with {file}.".format(file=self.__filename) + str(e)}, 500

    def __get_data_from_file(self):
        self.__filename = self.__file.filename
        self.__content_type = self.__file.content_type
        stream = io.StringIO(self.__file.stream.read().decode("UTF8"), newline=None)
        reader = csv.DictReader(stream)
        data_list = []

        for row in reader:
            # if empty replace with BLANK
            if not row['state']:
                row['state'] = 'BLANK'
            csv_data = CsvWebAppCsvModel(row['guid'], row['name'], row['first'], row['last'], row['email'],
                                         row['value'], row['date'], row['phone'], row['age'], row['state'],
                                         row['street'])
            data_list.append(csv_data)
