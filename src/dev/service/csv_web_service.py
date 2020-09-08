from flask import request, send_from_directory
from flask_restful import Resource
from dev.mgr.display_mgr import DisplayCsvManager
from dev.mgr.download_mgr import DownloadCsvManager
from dev.mgr.get_files_mgr import GetCsvFilesManager
from dev.mgr.stats_manager import PeopleStatsManager
from dev.mgr.upload_mgr import UploadCsvManager
from dev.util.helper.get_config import get_config_value


class Online(Resource):
    @classmethod
    def get(cls):
        return {'release': get_config_value('release_version'), 'Online': 'Yes'}


class CsvWebGetFilesService(Resource):

    @classmethod
    def get(cls):
        return GetCsvFilesManager().get_csv_files()


class CsvWebDisplayService(Resource):
    @classmethod
    def get(cls, filename):
        return DisplayCsvManager(filename).fetch_csv_data()


class CsvWebStatisticsService(Resource):
    @classmethod
    def get(cls, filename):
        return PeopleStatsManager(filename).get_persons_per_year()


class CsvWebDownloadService(Resource):
    @classmethod
    def get(cls, filename):
        msg = DownloadCsvManager(filename).prepare_csv_file()
        if msg['message'] == 'Done':
            return send_from_directory('../../temp', filename, as_attachment=True)
        else:
            return msg


class CsvWebUploadService(Resource):
    @classmethod
    def get(cls):
        return Online.get()

    @classmethod
    def post(cls):
        file = request.files['file']
        return UploadCsvManager(file).save_to_db()
