import uuid
from dev.db.db import db
from datetime import datetime
from dev.model.decorator.uuid import UUID
from dev.model.decorator.json_encoded_dict import JsonEncodedDict


class CsvWebAppModel(db.Model):
    __tablename__ = 'csv_web_app'

    filename = db.Column(db.String(), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    content_type = db.Column(db.String())
    csv_data = db.Column(JsonEncodedDict)

    def __init__(self, filename, content_type, csv_data):
        self.filename = filename
        self.content_type = content_type
        self.csv_data = csv_data

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_filename(cls, filename):
        return cls.query.filter_by(filename=filename).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
