from dev.db.db import db


class UUID(db.TypeDecorator):
    impl = db.Text

    def process_bind_param(self, value, dialect):
        return str(value)

    def process_result_value(self, value, dialect):
        return value
