import os
from dev.env.base_env import BaseEnvironment
import logging


class DevPostgresDB(BaseEnvironment):

    def log_init_message(self):
        logging.info("Running locally with a Postgres Database")

    def database_uri(self):
        self.app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('dev_local_postgres_db_uri')
