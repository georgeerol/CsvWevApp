from werkzeug.datastructures import FileStorage
from dev.mgr.upload_mgr import UploadManager
from dev.util.helper.get_config import get_config_value
from test.base_test import BaseTest


class UploadFileManagerTest(BaseTest):

    def test_process_file(self):
        with self.app_context():
            filename = 'test.csv'
            test_file = get_config_value('temp_download_folder') + '/' + filename

            file_to_Upload = FileStorage(stream=open(test_file, "rb"), filename=filename, content_type='text/csv')
            upload_mgr = UploadManager(file_to_Upload)
            actual_response = upload_mgr.save_to_db()
            self.assertEqual(({'message': 'Upload example_small.csv Successfully'}, 201), actual_response)
