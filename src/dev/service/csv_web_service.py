import logging
from flask import request
from flask_restful import Resource


class Online(Resource):
    @classmethod
    def get(cls):
        return {'release': '1.0', 'Online': 'Yes'}


class CsvWebService(Resource):
    @classmethod
    def get(cls):
        return Online.get()


    @classmethod
    def post(cls):
        data = request.get_data(as_text=True)
        print(data)
        return {'name': 'george'}
