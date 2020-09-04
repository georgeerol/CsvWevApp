import logging
import os
import io
import csv
from flask import request, send_from_directory
from flask_restful import Resource
from dev.model.csv_web_model import CsvWebAppFileModel, CsvWebAppCsvModel
from dev.stats.people_stats_manager import PeopleStatsManager
from dev.util.helper.get_config import get_config_value
from dev.mgr.upload_mgr import UploadManager


class Online(Resource):
    @classmethod
    def get(cls):
        return {'release': '1.0', 'Online': 'Yes'}


class CsvWebGetFilesService(Resource):

    @classmethod
    def get(cls):
        data_list = []
        model = CsvWebAppFileModel.find_all()
        for data in model:
            var = {"name": data.filename, "url": "http://localhost:5003/csvwebapp/files/{}".format(data.filename)}
            data_list.append(var)
        return data_list


class CsvWebDisplayService(Resource):
    @classmethod
    def get(cls, filename):
        model = CsvWebAppFileModel.find_by_filename(filename)
        dict_data = model.json()
        return dict_data


class CsvWebStatisticsService(Resource):
    @classmethod
    def get(cls, filename):
        print(filename)
        stats = PeopleStatsManager(filename)
        data = stats.get_persons_per_year()
        print(data)
        return data


class CsvWebDownloadService(Resource):
    @classmethod
    def get(cls, filename):
        model = CsvWebAppFileModel.find_by_filename(filename)
        dict_data = model.json()
        csv_columns = dict_data['csv_data'][0].keys()
        path = get_config_value('temp_download_folder')
        if not os.path.exists(path):
            os.makedirs(path)
        csv_file = filename
        try:
            with open(os.path.join(path, csv_file), 'w+') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for data in dict_data['csv_data']:
                    writer.writerow(data)
        except IOError:
            print("I/O error")
        # send the buffer as a regular file
        return send_from_directory('../../temp', filename, as_attachment=True)


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
        reader = csv.DictReader(stream)
        data_list = []

        for row in reader:
            # if empty replace with blank
            if not row['state']:
                row['state'] = 'BLANK'
            csv_data = CsvWebAppCsvModel(row['guid'], row['name'], row['first'], row['last'], row['email'],
                                         row['value'], row['date'], row['phone'], row['age'], row['state'],
                                         row['street'])
            data_list.append(csv_data)
        upload_mgr = UploadManager(filename, content_type, data_list)
        upload_mgr.save_to_db()
        return upload_mgr.get_response_message()
