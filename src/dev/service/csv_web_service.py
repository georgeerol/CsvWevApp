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


class CsvWebService(Resource):
    @classmethod
    def get(cls):
        return Online.get()

    @classmethod
    def post(cls):
        # data = request.get_data(as_text=True)
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
        data_dict = {"filename": filename, "data": csv_data, "type": content_type}
        print(data_dict)
        return {'name': 'george'}
