from datetime import datetime
from dev.db.db import db


class CsvWebAppFileModel(db.Model):
    __tablename__ = 'csv_web_app_file'

    filename = db.Column(db.String(), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    content_type = db.Column(db.String())
    csv_data = db.relationship('CsvWebAppCsvModel')

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


class CsvWebAppCsvModel(db.Model):
    __tablename__ = 'csv_web_app_csv'

    guid = db.Column(db.String(), primary_key=True)
    filename_id = db.Column(db.String, db.ForeignKey('csv_web_app_file.filename'))
    name = db.Column(db.String)
    first = db.Column(db.String)
    last = db.Column(db.String)
    email = db.Column(db.String)
    value = db.Column(db.String)
    date = db.Column(db.String)
    phone = db.Column(db.String)
    age = db.Column(db.String)
    state = db.Column(db.String)
    street = db.Column(db.String)

    def __init__(self, guid, name, first, last, email, value, date, phone, age, state, street):
        self.guid = guid
        self.name = name
        self.first = first
        self.last = last
        self.email = email
        self.value = value
        self.date = date
        self.phone = phone
        self.age = age
        self.state = state
        self.street = street

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def do_statistics(cls, filename,):
        print(filename)
        year = "2018"
        query = "select count(*) as people from (select count(*), date from {table}  where date like ?  and " \
                "filename_id = ? group by date ) ".format(table=cls.__tablename__)
        result = db.engine.execute(query, ("%{}".format(year),'example_small.csv'))
        return result.fetchone()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
