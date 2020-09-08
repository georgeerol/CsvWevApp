from datetime import datetime
from dev.db.db import db


class CsvWebAppFileModel(db.Model):
    __tablename__ = 'csv_web_app_file'

    filename = db.Column(db.String(), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    content_type = db.Column(db.String())
    csv_data = db.relationship('CsvWebAppCsvModel', lazy='dynamic')

    def __init__(self, filename, content_type, csv_data):
        self.filename = filename
        self.content_type = content_type
        self.csv_data = csv_data

    def json(self):
        return {'filename': self.filename, 'content_type': self.content_type,
                'csv_data': [row.json() for row in self.csv_data.all()]}

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
    id = db.Column(db.Integer, primary_key=True)
    filename_id = db.Column(db.String, db.ForeignKey('csv_web_app_file.filename'))
    guid = db.Column(db.String())
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

    def json(self):
        return {'guid': self.guid, 'name': self.name, 'first': self.first, 'last': self.last, 'email': self.email,
                'value': self.value, 'date': self.date, 'phone': self.phone, 'age': self.age, 'state': self.state,
                'street': self.street}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_year_list(cls, filename):
        unique_date_list = []

        query = db.session.query(cls.date).filter(cls.filename_id == filename).distinct().all()
        for dates in query:
            dt = datetime.strptime(dates[0], '%m/%d/%Y')
            if dt.year not in unique_date_list:
                unique_date_list.append(dt.year)
        unique_date_list.sort()
        return unique_date_list

    @classmethod
    def get_people_sum(cls, filename, year):
        query = "select count(*) as people from (select count(*), date from {table}  where date like ?  and " \
                "filename_id = ? group by date ) ".format(table=cls.__tablename__)

        result = db.engine.execute(query, ("%{}".format(year), filename))
        num_of_person = result.fetchone()
        return num_of_person

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
