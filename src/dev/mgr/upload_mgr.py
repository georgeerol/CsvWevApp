import csv
import io
import logging
from dev.model.csv_web_model import CsvWebAppFileModel, CsvWebAppCsvModel


class UploadCsvManager:

    def __init__(self, file):
        self.__file = file
        self.__filename = None
        self.__content_type = None
        self.__data_list = []

    def save_to_db(self):
        logging.info("Saving the csv file:{} to the database".format(self.__filename))
        self.__get_data_from_file()
        try:
            model = CsvWebAppFileModel(self.__filename, self.__content_type, self.__data_list)
            model.save_to_db()
            msg = 'Upload {file} Successfully'.format(file=self.__filename)
            logging.info(msg)
            return {'message': msg}, 201
        except Exception as e:
            error_msg = " Error  with {file}.".format(file=self.__filename) + str(e)
            logging.error(error_msg)
            return {'message': error_msg}, 500

    def __get_data_from_file(self):
        self.__filename = self.__file.filename
        self.__content_type = self.__file.content_type
        stream = io.StringIO(self.__file.stream.read().decode("UTF8"), newline=None)
        reader = csv.DictReader(stream)

        for row in reader:
            # if empty replace with BLANK
            if not row['state']:
                row['state'] = 'BLANK'
            csv_data = CsvWebAppCsvModel(row['guid'], row['name'], row['first'], row['last'], row['email'],
                                         row['value'], row['date'], row['phone'], row['age'], row['state'],
                                         row['street'])
            self.__data_list.append(csv_data)
