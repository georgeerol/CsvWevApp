import logging
import io
import csv
from flask import request
from flask_restful import Resource
from dev.model.csv_web_app_model import CsvWebAppModel


class Online(Resource):
    @classmethod
    def get(cls):
        return {'release': '1.0', 'Online': 'Yes'}


class CsvWebGetFilesService(Resource):

    @classmethod
    def get(cls):
        data_list = []
        model = CsvWebAppModel.find_all()
        for data in model:
            print(data.file_name)
            var = {"name": data.file_name, "url": "http://localhost:8087/files/{}".format(data.file_name)}
            data_list.append(var)
        return data_list


class CsvWebUploadService(Resource):
    @classmethod
    def get(cls):
        return Online.get()

    @classmethod
    def post(cls):
        f = request.files['file']
        filename = f.filename
        content_type = f.content_type
        stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
        csv_input = csv.reader(stream)
        iterip = iter(csv_input)
        next(iterip)
        csv_data = []
        for row in iterip:
            csv_data.append(row)
        csv_data_dict = {'csv_data': csv_data}
        model = CsvWebAppModel(filename, content_type, csv_data_dict)
        model.save_to_db()
        dict_message = {'message': 'Update the file successfully: {}'.format(filename)}
        return dict_message
