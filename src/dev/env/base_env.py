from abc import abstractmethod
import os
from dotenv import load_dotenv
from dev.setup.app_setup import AppSetup
from dev.db.db import db
from dev.util.logger import logger
from flask import Flask

app = Flask(__name__)
from flask_cors import CORS
load_dotenv()
cors = CORS(app, resources={r"/csvwebapp/*": {"origins": "*"}})


class BaseEnvironment:
    def __init__(self):
        self.app = app
        self.db = db
        self.host = os.getenv('app_host')
        self.port = os.getenv('app_port')

    def build(self):
        self.log_setup()
        self.env()
        self.database_uri()
        self.track_modifications()
        self.propagate_exceptions()
        self.debug()
        self.test()
        self.init()

    @staticmethod
    def log_setup():
        logger.setup_log()

    @abstractmethod
    def database_uri(self):
        raise NotImplementedError("database_config() must be defined in subclass")

    @abstractmethod
    def log_init_message(self):
        raise NotImplementedError("log_init_message() must be defined in subclass")

    def track_modifications(self, sql_track_mod=False):
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = sql_track_mod

    def propagate_exceptions(self, prop_except=True):
        # To allow flask propagating exception even if debug is set to false on app
        self.app.config['PROPAGATE_EXCEPTIONS'] = prop_except

    def env(self):
        self.app.config['ENV'] = os.getenv('app_env')

    def debug(self, debug=True):
        self.app.config['DEBUG'] = debug

    def test(self, test=True):
        self.app.config['TESTING'] = test

    def init(self):
        self.db.init_app(self.app)
        AppSetup().init()

    def first_request(self):
        @self.app.before_first_request
        def create_table():
            self.db.create_all()

    def get_host(self):
        return self.host

    def get_port(self):
        return self.port
