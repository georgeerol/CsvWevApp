import csv
import io
from flask import request
from flask_restful import Resource
from dev.mgr.download_mgr import DownloadManager
from dev.mgr.stats_manager import PeopleStatsManager
from dev.mgr.upload_mgr import UploadManager
from dev.mgr.display_mgr import DisplayManager
from dev.model.csv_web_model import CsvWebAppFileModel, CsvWebAppCsvModel


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
        display_mgr =DisplayManager(filename)
        return display_mgr.fetch_csv_data()


class CsvWebStatisticsService(Resource):
    @classmethod
    def get(cls, filename):
        stats = PeopleStatsManager(filename)
        return stats.get_persons_per_year()


class CsvWebDownloadService(Resource):
    @classmethod
    def get(cls, filename):
        download_mgr = DownloadManager(filename)
        return download_mgr.process_file()


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
            # if empty replace with BLANK
            if not row['state']:
                row['state'] = 'BLANK'
            csv_data = CsvWebAppCsvModel(row['guid'], row['name'], row['first'], row['last'], row['email'],
                                         row['value'], row['date'], row['phone'], row['age'], row['state'],
                                         row['street'])
            data_list.append(csv_data)
        upload_mgr = UploadManager(filename, content_type, data_list)
        return upload_mgr.save_to_db()
