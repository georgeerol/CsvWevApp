import os
import logging
from dev.model.csv_web_model import CsvWebAppFileModel


class GetCsvFilesManager:
    def __init__(self):
        self.__csv_files = []

    def get_csv_files(self):
        logging.info("Getting csv files")
        try:
            model = CsvWebAppFileModel.find_all()
            for data in model:
                var = {"name": data.filename,
                       "url": "http://{host}:{port}/csvwebapp/files/{filename}".format(host=os.getenv('app_host'),
                                                                                       port=os.getenv('app_port'),
                                                                                       filename=data.filename)}
                self.__csv_files.append(var)
            return self.__csv_files
        except Exception as e:
            error_msg = " Error fetching csv files" + str(e)
            logging.error(error_msg)
            return {'message': error_msg}, 500
