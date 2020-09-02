import os

from dotenv import load_dotenv
from flask_restful import Api

from dev.env.base_env import app
from dev.env.dev_postgres_db import DevPostgresDB
from dev.env.dev_sqllite_db import DevSqlLiteDB
from dev.service.csv_web_service import CsvWebUploadService, CsvWebGetFilesService, CsvWebDownloadService, \
    CsvWebDisplayService , CsvWebStatisticsService
from dev.service.csv_web_service import Online
from dev.util.helper.get_config import get_config_value

load_dotenv()

if os.environ.get("app_env") == 'dev_postgres_db':
    env = DevPostgresDB()
else:
    env = DevSqlLiteDB()
env.build()

HOST = env.get_host()
PORT = env.get_port()

flask_api = Api(app)
flask_api.add_resource(CsvWebUploadService, get_config_value('upload_file_url_path'))
flask_api.add_resource(CsvWebGetFilesService, get_config_value('get_list_of_files'))
flask_api.add_resource(CsvWebDownloadService, get_config_value('download_a_file'))
flask_api.add_resource(CsvWebDisplayService, get_config_value('display_a_file'))
flask_api.add_resource(CsvWebStatisticsService,get_config_value('data_statistics'))
flask_api.add_resource(Online, '/')

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
