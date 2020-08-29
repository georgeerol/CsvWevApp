import os
from dev.env.base_env import BaseEnvironment
import logging


class DevSqlLiteDB(BaseEnvironment):

    def log_init_message(self):
        logging.info("Running locally with a sqllite Database")

    def database_uri(self):
        self.app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('dev_local_sqllite_db_uri')
