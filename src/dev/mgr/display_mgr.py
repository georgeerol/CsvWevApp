import logging
from dev.model.csv_web_model import CsvWebAppFileModel


class DisplayCsvManager:

    def __init__(self, filename):
        self.__filename = filename

    def fetch_csv_data(self):
        logging.info("Fetching display csv data ")
        try:
            model = CsvWebAppFileModel.find_by_filename(self.__filename)
            dict_data = model.json()
            msg = 'Display {file} Successfully'.format(file=self.__filename)
            logging.info(msg)
            dict_data['message'] = msg
            return dict_data
        except Exception as e:
            err_msg = " Error displaying csv {file}.".format(file=self.__filename) + str(e)
            logging.error(err_msg)
            return {'message': err_msg}, 500
