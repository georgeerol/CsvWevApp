import csv
import io
from flask import request
from flask_restful import Resource
from dev.mgr.display_mgr import DisplayManager
from dev.mgr.download_mgr import DownloadManager
from dev.mgr.get_files_mgr import GetCsvFilesManager
from dev.mgr.stats_manager import PeopleStatsManager
from dev.mgr.upload_mgr import UploadManager
from dev.model.csv_web_model import CsvWebAppCsvModel


class Online(Resource):
    @classmethod
    def get(cls):
        return {'release': '1.0', 'Online': 'Yes'}


class CsvWebGetFilesService(Resource):

    @classmethod
    def get(cls):
        return GetCsvFilesManager().fetch_csv_data()


class CsvWebDisplayService(Resource):
    @classmethod
    def get(cls, filename):
        return DisplayManager(filename).fetch_csv_data()


class CsvWebStatisticsService(Resource):
    @classmethod
    def get(cls, filename):
        return PeopleStatsManager(filename).get_persons_per_year()


class CsvWebDownloadService(Resource):
    @classmethod
    def get(cls, filename):
        return DownloadManager(filename).process_file()


class CsvWebUploadService(Resource):
    @classmethod
    def get(cls):
        return Online.get()

    @classmethod
    def post(cls):
        file = request.files['file']
        return UploadManager(file).save_to_db()
