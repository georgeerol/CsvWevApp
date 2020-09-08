import io
from app import app
from test.base_test import BaseTest
from werkzeug.datastructures import FileStorage
from dev.util.helper.get_config import get_config_value


class CsvWebUploadService(BaseTest):

    def test_upload_service(self):
        url_path = get_config_value("upload_file_url_path")
        filename = 'upload_test.csv'
        test_file = get_config_value('temp_download_folder') + '/' + filename
        file_to_Upload = FileStorage(stream=open(test_file, "rb"), filename=filename, content_type='text/csv')
        data = {'file': file_to_Upload}
        with app.test_client() as c:
            resp = c.post(url_path, data=data, content_type='multipart/form-data')
            self.assertEqual(201, resp.status_code)
