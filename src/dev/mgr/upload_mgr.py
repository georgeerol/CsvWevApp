from dev.model.csv_web_model import CsvWebAppFileModel


class UploadManager:

    def __init__(self, filename, content_type, data_list):
        self.__filename = filename
        self.__content_type = content_type
        self.__data_list = data_list
        self.__response_message = {}, 500

    def save_to_db(self):
        try:
            model = CsvWebAppFileModel(self.__filename, self.__content_type, self.__data_list)
            model.save_to_db()
            self.__response_message = {'message': 'Upload {file} Successfully'.format(file=self.__filename)}, 201
        except Exception as e:
            self.__response_message = {'message': " Error  with {file}.".format(file=self.__filename) + str(e)}, 500

    def get_response_message(self):
        return self.__response_message
