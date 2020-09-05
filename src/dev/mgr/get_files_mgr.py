from dev.model.csv_web_model import CsvWebAppFileModel


class GetCsvFilesManager:
    def __init__(self):
        self.__data_list = []

    def fetch_csv_data(self):
        try:
            model = CsvWebAppFileModel.find_all()
            for data in model:
                var = {"name": data.filename, "url": "http://localhost:5003/csvwebapp/files/{}".format(data.filename)}
                self.__data_list.append(var)
            return self.__data_list
        except Exception as e:
            return {'message': " Error fetching csv files" + str(e)}, 500
