from dev.model.csv_web_model import CsvWebAppFileModel


class UploadManager:

    def __init__(self, filename, content_type, data_list):
        self.__filename = filename
        self.__content_type = content_type
        self.__data_list = data_list

    def save_to_db(self):
        try:
            model = CsvWebAppFileModel(self.__filename, self.__content_type, self.__data_list)
            model.save_to_db()
            return {'message': 'Upload {file} Successfully'.format(file=self.__filename)}, 201
        except Exception as e:
            return {'message': " Error  with {file}.".format(file=self.__filename) + str(e)}, 500
